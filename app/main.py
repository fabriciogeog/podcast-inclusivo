from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import requests

API_URL = "http://127.0.0.1:8000"   # Endereço local do backend

# ----------------------------------------------------------------------
# Telas
# ----------------------------------------------------------------------

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        layout.add_widget(Label(
            text="🔍 Buscar Notícias",
            font_size=28,
            halign="center"
        ))

        btn_test_api = Button(
            text="Testar conexão com o backend",
            size_hint=(1, 0.2)
        )
        btn_test_api.bind(on_release=self.test_backend)

        btn_open_results = Button(
            text="Abrir resultados iniciais",
            size_hint=(1, 0.2)
        )
        btn_open_results.bind(on_release=self.goto_results)

        layout.add_widget(btn_test_api)
        layout.add_widget(btn_open_results)

        self.output = Label(text="", font_size=18)
        layout.add_widget(self.output)

        self.add_widget(layout)


    def test_backend(self, instance):
        try:
            r = requests.get(f"{API_URL}/status", timeout=5)
            data = r.json()
            self.output.text = f"API OK: {data['message']}"
        except Exception as e:
            self.output.text = f"Erro: {e}"


    def goto_results(self, instance):
        self.manager.current = "results"


class ResultsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        layout.add_widget(Label(
            text="Resultados da Pesquisa",
            font_size=28
        ))

        btn_back = Button(
            text="Voltar",
            size_hint=(1, 0.2)
        )
        btn_back.bind(on_release=self.go_back)

        layout.add_widget(btn_back)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = "home"


# ----------------------------------------------------------------------
# App Principal
# ----------------------------------------------------------------------

class AccessibleNewsApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ResultsScreen(name="results"))

        return sm


if __name__ == "__main__":
    AccessibleNewsApp().run()
