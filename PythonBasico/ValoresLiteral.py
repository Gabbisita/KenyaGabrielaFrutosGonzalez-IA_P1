# --> Mutabilidad de las Variables: El Concepto de un Comeback <--

# Una variable es como el concepto de un grupo: puede cambiar.
# Primero, la variable 'concepto_actual' es "Dark".
concepto_actual = "Dark y misterioso"
print(f"El concepto de este comeback es: {concepto_actual}")

# Para el siguiente comeback, el valor de la misma variable se actualiza.
# El valor anterior se pierde y es reemplazado por el nuevo.
concepto_actual = "Fresco y veraniego"
print(f"El nuevo concepto para el verano es: {concepto_actual}")


# --> Literales: Valores sin Variable <--

# Un "literal" es un valor escrito directamente en el código que no se guarda en ninguna variable.
# Es como un fanchant que se grita en un concierto: existe en ese momento, pero no se almacena en ningún lado.
"Stray Kids, woah!" # Esto es un literal de tipo string. Python lo lee y no hace nada con él.
1997               # Esto es un literal de tipo numérico.

# Normalmente, los literales se usan para asignarlos a variables o pasarlos a funciones.
año_debut = 2018
print("El año de debut fue:", año_debut) # Aquí, 2018 y el texto son literales que se usan en la función print.
