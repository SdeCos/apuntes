## **Convenciones**

### **Generales**

1. Todos los predicados van en minúsculas
2. Los valores tipo cadenas van entre comillas dobles (ver notaciones al final de la página)
3. Todas las relaciones van con letra inicial mayúscula y entre paréntisis ( y )

4. Al incluir el nombre de la base de datos en un predicado se debe utilizar el punto y todo el predicado en minúsculas.

   > Ej r.campoid y no R.campoid

### **Relaciones unarias**

#### **Selección**

1. Todos los predicados de la selección se colocan entre guiones bajos (\_).

   > Ej σ*campoid=valor*(R)

2. Si el campo en cuestión, tiene guiones bajos originalmente, estos se eliminaran en el momento de hacer la consulta.

   > Ej En la relación original: campo_id;en la consulta se sustituye por campoid

3. La selección no incluye espacios en blanco aunque contemple operadores

   > Ej σ*campoid>valor^campoid<=valor*(R)

4. Todos los predicados de la selección se separan por operadores.

   > Ej σ*campoid>valor^campoid<=valor*(R)

5. Entre el último atributo de la selección y la relación hay un guión bajo.

#### **Proyección**

1. Entre una proyección y una selección hay un espacio en blanco.

   > Ej Πv.id,pr.nombre,v.cantidad σ*v.cantidad>9*(R)

2. La proyección no incluye espacios en blanco entre sus atributos

   > Ej Πv.id,pr.nombre,v.cantidad

3. Los atributos de la proyección se separan por comas

   > Ej Πv.id,pr.nombre,v.cantidad

4. Entre los atributos de una proyección y un renombramiento hay un espacio en blanco

   > Ej Πproveedores.nombre_pR3(R1)

### **Agregaciones**

1. En las agregaciones, la G caligráfica queda separada por guiones bajos de los atributos que la rodean. Al mismo tiempo la relación objetivo de la Agregación se separa con un guión bajo.

### **Relaciones Binarias**

#### **Operaciones**

1. Las operaciones entre dos relaciones binarias R1 y R2 se colocan sin espacios

   > Ej (R1:R2)

2. El resultado de una relación binaria es otra relación

   > Ej Πproveedores.nombre_pR3(R1:R2)

3. El valor de una relación binaria es el registro asociado a su resultado.

   > Ej Javier

4. En las operaciones binarias con varios pasos, las relaciones reaultantes de cada paso deben ser renombradas con la letra R mayúscula y el número correspondiente y una salida output con el o los valores resultantes.

   > Ej
   > Paso 1: Πr1.atributo1,r1.atributo2,r2.atributo3 σr1.atributo1>9_pR1(R⋈S)

   > Paso 2: Πr2.atributo_pR2(O)

   > Paso 3: Πr3.nombre_pR3(R1:R2)

   > Output : Javier

## Notaciones Álgebra Relacional

1. Selección: σ
2. Proyección: Π
3. Reunión: ⋈
4. Reunión Externa por la izquierda: ⟕
5. Reunión Externa por la derecha: (⟖)
6. Producto Cartesiano : x
7. Unión: ∪
8. Intersección: ∩
9. Renombramiento: p
10. División: ÷
11. Diferencia: -
12. Comillas dobles: " "
13. Agregación : Ģ

## Operadores relacionales

1. Mayor qué: >
2. Menor qué: <
3. Mayor o igual qué: ≥
4. Menor e igual qué: ≤
5. Igual qué: =
6. Multiplicación: \*

## Operadores Lógicos

1. AND : ^
2. OR: 🇻
3. NOT: ㄱ
