# subject-classification-spanish


[![PyPI version](https://badge.fury.io/py/subject-classification-spanish.svg)](https://badge.fury.io/py/subject-classification-spanish)

# How does it work?

subject-classification-spanish is a python library that uses convolutional neural networks to predict the subject (politics, sports, health...) of spanish sentences. The model was trained using over *1000000* news from the main spanish newspapers *el pais, el mundo, abc, la vanguardia, 20 minutos and publico*.
This news were extracted using web scraping with the project [news-scrapers-workers-go](https://github.com/news-scrapers/news-scraper-workers-go)

Using the tags in the news we trained the model to learn from the language in them. For that we use the libraries Keras and Tensorflow and sklearn.
For more details regarding the training of the neural network model check the repo [news-scraper-subject-classifiers-model](https://github.com/news-scrapers/news-scraper-subject-classifiers-model) 

# Why?

I believe there are not many solutions to subject classification analysis **in spanish** based on neural networks.


# Install and use

First to install the package

```
pip install subject-classification-spanish
```

You will also need keras, tensorflow and sklearn

```
pip install keras tensorflow sklearn
```

Import the package

```
from subject_classification_spanish import subject_classifier

```

for instance, using this text extracted from a politics new:

```
text_text_politics = "La entrada en el 2020 ha comportado cambios en la edad de jubilación y en el cálculo de los años cotizados que se tienen en cuenta para determinar la prestación. Las medidas son de carácter automático, ya que forman parte de la reforma de 2011 que hace que la edad para jubilarse se retrase paulatinamente hasta llegar a los 67 años.  ADVERTISING  Todo esto se da mientras resta pendiente saber cuál será la subida de las prestaciones en el 2020, ya que aunque el Gobierno en funciones ha prometido que se subirán el 0,9% y no perderán poder adquisitivo, la medida no se tomará hasta que esté formado un Ejecutivo. En diciembre de 2019 en España se contabilizaban 6.089.294 pensiones de jubilación, con una prestación media de 1.143,55 euros mensuales.   Pensiones en 2020 Los cambios en la edad de jubilación  Respecto a la edad de jubilación, cada año se va retrasando en virtud del régimen establecido en la reforma de 2011 aprobada durante el mandato de José Luis Rodríguez Zapatero. De esta forma, en 2020 la edad legal ordinaria será de 65 años y 10 meses. Esta edad se aplicará a aquellos que han cotizado menos de 37 años.  Si una persona llega a los 65 años en 2020 y ha cotizado 37 años o más, ya podrá jubilarse con 65 años.  En el caso de la jubilación parcial, en la que se combina trabajo y prestación, el mínimo será de 61 años y 10 meses con 35 años o más cotizados; o de 62 años y 8 meses con 33 años cotizados.  Con cada año que pasa es necesaria más edad para acceder a la jubilación, tanto si se ha cotizado por encima o por debajo de los periodos de referencia  Con cada año que pasa es necesaria más edad para acceder a la jubilación, tanto si se ha cotizado por encima o por debajo de los periodos de referencia Pensiones en 2020 Los cambios en el cálculo de la pensión  Por lo que respecta al cálculo de la pensión que se cobrará la momento de jubilarse, en 2020 se tendrán en cuenta los últimos 23 años cotizados. Estos años cotizados conforman la base reguladora, que es la suma de las bases de cotización en dicho periodo. Hay que tener en cuenta que cuantos más años se tengan en cuenta es posible que se recorte más la pensión, ya que en los últimos años de vida laboral es cuando mejores salarios se suelen cobrar.   Esta es otra de las reformas introducidas con los cambios en las pensiones de la década anterior, momento hasta el que se tenían en cuenta los últimos 15 años trabajados. La idea es que para 2022 ya se tengan en cuenta los últimos 25 años cotizados. De esta manera, en 2021 se computarán los últimos 24 años trabajados y en 2022 los últimos 25 años cotizados.  La base reguladora de la pensión se obtiene de dividir los meses de los años exigidos por el divisor correspondiente La base reguladora de la pensión se obtiene de dividir los meses de los años exigidos por el divisor correspondiente (LV) En 2023 El recorte de las pensiones que viene  Otra de las medidas que tendrán un fuerte calado en el sistema es la llegada del factor de sostenibilidad, que se aplicará a partir de 2023 e irá recortando las nuevas pensiones, teniendo en cuenta que los pensionistas vivirán más. Dicha medida en un principio debía aplicarse en 2019.  El conjunto de medidas se puede consultar al detalle en la guía para la jubilación del Ministerio de Trabajo, Migraciones y Seguridad Social."

```

create the new classifier:

```
classifier = SubjectClassifier()

```

run the subject analysis:

```
classes_result = classifier.classify(text_text_politics)
print(classes_result)


```

you will see that it outputs a dictionary with the detected subjects and its probabilities

```
{'trabajo': 0.06324339, 'política laboral': 0.062398944, 'seguridad social': 0.04280818, 'pensiones': 0.033200286, 'sindicatos': 0.030516632, 'prestaciones': 0.026752898, 'sindicalismo': 0.02659354, 'empleo': 0.024692126, 'condiciones trabajo': 0.02205481, 'cc oo': 0.01712212}
```

For instance if you this football new

```
text_text_football =  "Buenas noticias para el Atlético de Madrid a expensas de que la crisis sanitaria provocada por el Covid19 permita volver a la actividad normal en todo el país y eso suponga también el regreso del fútbol. Sabiendo que ahora mismo no es lo más importante, la vuelta de la competición constataría que se ha podido superar esta pesadilla generada por el coronavirus. El caso es que, de momento, el Atlético de Madrid ya sabe que podrá contar con uno de sus hombres más importantes, con Álvaro Morata . El jugador ha aprovechado estas semanas de parón para recuperarse de la lesión que se produjo el pasado 11 de marzo en el partido que el equipo colchonero disputó ante el Liverpool en Anfield Road. Antes de esa cita, el futbolista se lesionaba 15 días antes del partido de ida de los octavos de final ante el Liverpool y tuvo que trabajar contrarreloj para recuperarse. Lo consiguió, claro, pero era evidente que estaba jugando con molestias. Encima, en el choque posterior ante el Sevilla se llevó varios golpes, uno en el glúteo y otro en una de sus piernas, que le hicieron ser seria duda para la cita de Anfield, a la que llegó mermado. De ahí que se acabase lesionando pese a marcar el gol de la victoria. Pues bien, el jugador ya cuenta con el alta médica, según explicó hace unos días el diario Marca. Eso quiere decir que ya está para entrenarse como el resto de compañeros, con algo más de intensidad, dentro del programa que el cuerpo técnico rojiblanco ha transmitido a los futbolistas. El futbolista se tuvo que recuperar en casa a cuenta del confinamiento, pero el club colchonero le puso a su disposición material de fisioterapia, presoterapia, crioterapia y electroestimulación para pasar este trance y cuenta con el seguimiento diario y asesoramiento de los profesionales del club, de los recuperadores del equipo así como del jefe de los servicios médicos."


```

run the subject analysis:

```
classes_result = classifier.classify(text_text_football)
print(classes_result)

```

you will see that it outputs:

```
{'atlético madrid': 0.36974072, 'real madrid': 0.25722897, 'fútbol': 0.075289354, 'deportes': 0.038075462, 'futbolistas': 0.029724792, 'baloncesto': 0.025478985, 'fc barcelona': 0.02337921, 'jugadores': 0.021244459, 'equipos': 0.015159458, 'primera división': 0.013489615}
```

## Customization
The function ``classify(text)`` admits an input ``default_threshold`` . This is the lowest probability of the subject you want to display. By default is 0.001. 

## Output and meaning
The function ``classify(text)`` a dictionary wich has all the subjects as keys and the probabilities as values a number between 0 and 1.