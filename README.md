Proyecto para ser corregido por Daniel Riverol de Talento Tech - Agencia de Habilidades para el Futuro

Devolución: 
Muy bien!
Tu código está muy prolijo, sin embargo tiene 2 problemas principales:
En "Agregar" (Opción 1): Si el usuario se equivoca en el precio (pone "mil"), tu código le descarta todo (nombre y categoría) y lo manda al menú. Es frustrante.
Usá un bucle while True para cada dato (nombre, categoría y precio) para que el usuario solo repita la parte que hizo mal.
En "Agregar" y "Buscar" (Opciones 1 y 3): Estás usando .isalpha() para validar el nombre. Eso es demasiado estricto: no te deja poner espacios ni números (como "Coca Cola", "Remera L" o "Intel i5").
Sacá el .isalpha() y solo validá que el campo no esté vacío (if nombre != "").



