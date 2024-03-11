Cabecera
========


Parrafos
--------

Para escribir parrafos solo tenemos que escribir sin marcar. Si queremos remarcar con *cursiva*. La **negrita** es con
doble asterisco. Para ejemplos de codigo las dobles comillas ``print("Hola Mundo")``.

* No puede estar submetidos
* Los contenidos no pueden comenzar con un espacio en blanco. * texto* no funciona
* Tiene que estar separado por caracteres separadores. Puede usar la barra de escape para permitir unir palabaras : Esto\ **Es**\una palabra

.. _nivelSecciones:

Niveles de secciones.
---------------------

Los distintos niveles de seccion se escriben de la siguiente forma:

* = para secciones.
* "-" para subsecciones.
* ^ para subsubsecciones.
* " para parrafos.

Listas
------

Las listas se marcan con * al principio.

Listas Desordenadas
^^^^^^^^^^^^^^^^^^^

* Lista Simple
* Otro elemento de la lista

 * con subniveles
 * muy facilemente

Listas Ordenadas
^^^^^^^^^^^^^^^^

1. Primer elemento.
2. Segundo elemento.

 2.1. Subelemento
 2.2. Otro subelemento

#. Otro tipo de lista
#. Ordenada

Listas de definiciones
^^^^^^^^^^^^^^^^^^^^^^

Termino (primera linea de texto)
 Definción del termino, que tiene que estar tabulado

 Puede tener varias linea o varios parrafos.
Siguiente termino
 Con su definición.

Bloques Literales
^^^^^^^^^^^^^^^^^

Despues de un texto normal, podemos dejar un parrafo con un ejemplo de codigo::

 def hola_mundo():
     print("Hola Mundo")
     return None

 def adios_mundo():
     print("Adios Mundo")

El texto continua normal despues del bloquea.

Bloques Doctest
^^^^^^^^^^^^^^^

Para los bloques de Doctest no requieren ninguna marca especial.

 >>> 1 + 1
 2

Hipervinculos
^^^^^^^^^^^^^

Enlaces externos
````````````````

Podemos consultar la documentacion de uso de `restructuredtext <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ para consultar la ayuda.

El parrafo tiene un enlace a la pagina principal de `Daniel Castelao`_.

.. _Daniel Castelao: https://www.danielcastelao.org

Enlaces internos
````````````````
Puedo hacer referencias con una etiqueta colocada arriba con :ref:`nivelSecciones`.


Tablas
^^^^^^

+----------------------------+-----------+-----------+-----------+
|Cabecera fila 1 , columna 1 | Cabecera2 | Cabecera3 | Cabecera4 |
+============================+===========+===========+===========+
|Contenido fila 1, columna 1 | Columna 2 | Columna 3 | Columna 4 |
+----------------------------+-----------+-----------+-----------+
|Contenido fila 2, columna 1 | Columna 2 | Columna 3 | Columna 4 |
+----------------------------+-----------+-----------+-----------+

Otra forma mas facil.

========= ======== ========= ========= =========
Lunes     Martes   Miercoles Jueves    Viernes
========= ======== ========= ========= =========
Libre     DI       PMDM      Libre     Libre
DI        DI       PMDM      Libre     Libre
DI        DI       PMDM      Libre     Libre
DI        Libre    Libre     Libre     Libre
Descanso  Descanso Descanso  Descanso  Descanso
SXE       Libre    Libre     Libre     Libre
SXE       Libre    Libre     Libre     Libre
SXE       Libre    Libre     Libre     Libre
========= ======== ========= ========= =========


Imagenes
^^^^^^^^

Ahora la imagen 'panda' que esta en source/static/panda.jpg

.. image:: _static/panda.jpg
   :width: 200px
   :height: 200px
   :scale: 50 %
   :alt: Imagen de giu

Notas de pie
^^^^^^^^^^^^

Este texto esta realizado con Sphinx [#n1]_ para realizar la documentacion.

.. rubric:: Notas

.. [#n1] Pueden encontrar mas informacion en Sphinx_

.. _Sphinx: https://www.sphinx-doc.org


.. Danger::
    Cuidado con esto...

.. Attention::
    Fijense en la estructura.

.. Caution::
    Sigan alerta!

.. Important::
    Prestan atencion a esto.

.. tip::
    Este truco es resaltable.

..
   Las posibilidades son:
   Attention, caution, danger, error, hint, important, tip, warning.