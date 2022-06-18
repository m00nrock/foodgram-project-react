from django.db.models import Sum
from django.http import HttpResponse
from recipes.models import IngredientRecipe
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from rest_framework import permissions, viewsets


class CartDownload(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def canvas_method(dictionary):
        response = HttpResponse(content_type='application/pdf')
        response[
            'Content-Disposition'] = 'attachment; \
        filename = "shopping_cart.pdf"'
        begin_position_x, begin_position_y = 40, 650
        sheet = canvas.Canvas(response, pagesize=A4)
        pdfmetrics.registerFont(TTFont('Montserrat',
                                       'data/Montserrat.ttf'))
        sheet.setFont('Montserrat', 50)
        sheet.setTitle('Список покупок')
        sheet.drawString(begin_position_x,
                         begin_position_y + 40, 'Список покупок: ')
        sheet.setFont('FreeSans', 24)
        for number, item in enumerate(dictionary, start=1):
            if begin_position_y < 100:
                begin_position_y = 700
                sheet.showPage()
                sheet.setFont('Montserrat', 24)
            sheet.drawString(
                begin_position_x,
                begin_position_y,
                f'{number}.  {item["ingredient__name"]} - '
                f'{item["ingredient_total"]}'
                f' {item["ingredient__unit"]}'
            )
            begin_position_y -= 30
        sheet.showPage()
        sheet.save()
        return response

    def download(self, request):
        result = IngredientRecipe.objects.filter(
            recipe__carts__user=request.user).values(
            'ingredient__name', 'ingredient__measurement_unit').order_by(
                'ingredient__name').annotate(ingredient_total=Sum('amount'))
        return self.canvas_method(result)
