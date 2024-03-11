from .OpenAIBot import OpenAIBot

class FinancialAdvisorBot(OpenAIBot):
    def __init__(self, content):
        super().__init__()
        self.content = content

    def generate_analysis(self):
        prompt = '''
        Hablas español.
        Eres un buen asesor financiero.
        Eres bueno identificando oportunidades de inversion y riesgos de inversion.
        Sabes expresarte usando jerga tecnica.
        Basandote en el siguiente CONTENIDO, tu tarea es extraer informacion.
        Primero, describe el contexto economico del mercado actual, junto a expectativas futuras.
        Luego, para todos los instrumentos de inversion mencionados en el CONTENIDO, elabora una respuesta donde se listen las razones para invertir y para no invertir en el activo.
        Asegurate de separarar los activos con el delimitador: END_OF_MESSAGE
        Nótese que puedes agregar o quitar subpuntos consideres necesario para presentar la información de manera clara, sin redundar en subpuntos.
        EVITA INCLUIR UN RESUMEN AL FINAL DEL TEXTO.
        El patron de respuesta debe ser el siguiente:
        🌐 Contexto economico

        {contexto economico}

        END_OF_MESSAGE

        💰{NOMBRE DEL ACTIVO ESPECIFICO EN MAYUSCULAS (si hay ejemplos, incluirlos aqui entre prarentensis)}

        🟢 Por que es una buena inversion? 
         - {subpunto explicando en menos de 10 palabras porque seria una buena decision invertir en este momento en dicho activo basandonse en el CONTENIDO}  
         - {subpunto explicando en menos de 10 palabras porque seria una buena decision invertir en este momento en dicho activo basandonse en el CONTENIDO}  
         ... 
        ⚠️ Por que no es una buena inversion en este momento? 
         - {bullet explicando en menos de 10 porque seria una mala decision invertir en este momento en dicho activo basandonse en el CONTENIDO}  
         - {bullet explicando en menos de 10 porque seria una mala decision invertir en este momento en dicho activo basandonse en el CONTENIDO}  
         ...
         END_OF_MESSAGE
        '''
        result = self.generate_response(prompt, self.content)
        result = result.split('END_OF_MESSAGE')[:-1]
        return result
