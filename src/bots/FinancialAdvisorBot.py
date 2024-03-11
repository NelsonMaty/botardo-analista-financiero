from .OpenAIBot import OpenAIBot

class FinancialAdvisorBot(OpenAIBot):
    def __init__(self, content):
        super().__init__()
        self.content = content

    def generate_analysis(self):
        prompt = '''
        Hablas español.
        Basandote en el siguiente CONTENIDO, tu tarea es extraer informacion precisa acerca de oportunidades y riesgos de inversion.
        Primero, describe el contexto economico del mercado actual, junto a expectativas futuras.
        Luego, enumera todos los nombres de activos de inversion mencionados en el CONTENIDO.
        Siguiente, para cada uno de esos nombres de activos de inversion elabora hasta dos parrafos. 
        El primer parrafo lista las razones para invertir en el instrumento. 
        El segundo parrafo lista las razones para no invertir en el instrumento.
        Asegurate de separarar los activos con el delimitador: END_OF_MESSAGE
        Nótese que puedes agregar o quitar items en los listados como necesites para presentar la información completa.
        Evita incluir un resumen al final del texto.
        El patron de respuesta debe ser el siguiente:
        🌐 Contexto economico

        {contexto economico en terminos tecnicos. Expectativas mencionadas para el futuro.}

        END_OF_MESSAGE

        💰{NOMBRE DEL ACTIVO ESPECIFICO EN MAYUSCULAS (si hay ejemplos, incluirlos aqui entre prarentensis)}

        🟢 Por que es una buena inversion? 
         - {item de listado explicando en menos de 10 palabras porque seria una buena decision invertir en este momento en dicho activo basandonse en el CONTENIDO}
         ... 
        ⚠️ Por que no es una buena inversion en este momento? 
         - {item de listado explicando en menos de 10 palabras porque seria una mala decision invertir en este momento en dicho activo basandonse en el CONTENIDO}
         ...
         END_OF_MESSAGE
        '''
        result = self.generate_response(prompt, self.content)
        result = result.split('END_OF_MESSAGE')[:-1]
        return result
