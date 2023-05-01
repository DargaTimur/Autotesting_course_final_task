from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # иниц. Page Object, передаем в констр. экз. драйвера и url адрес 

    page = MainPage(browser, link) 
    page.open_page() # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина

# pytest -v --tb=line --language=en c:\Users\Timur\Autotesting_course_final_task\test_main_page.py