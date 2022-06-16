import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_offer', [n if n != 7 else pytest.param(n, marks=pytest.mark.xfail) for n in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.book_in_basket()
    page.correct_price_in_basket()
