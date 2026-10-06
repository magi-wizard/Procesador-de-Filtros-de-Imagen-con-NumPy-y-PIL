# Procesador de Filtros de Imagen con NumPy y PIL

Aplicación modular por línea de comandos (CLI) desarrollada en Python para la aplicación de filtros y transformaciones digitales sobre imágenes, utilizando manipulación directa de matrices de píxeles mediante **NumPy**, **PIL (Pillow)** y **Matplotlib**.

---

## 📌 Características Principales

* **Escala de Grises:** Proyección monocromática mediante el promedio de los tres canales de color sobre el tercer eje (`axis=2`).
* **Inversión de Colores (Negativo):** Transformación aritmética directa del espacio de color (`255 - I`).
* **Ajuste de Brillo:** Desplazamiento lineal de la luminosidad con conversión preventiva a `int16` y truncamiento con `np.clip` para evitar desbordamientos (*overflow/underflow*).
* **Ajuste de Contraste:** Expansión y compresión del rango dinámico respecto al punto medio ($128.0$) usando operaciones en coma flotante (`float32`).
* **Efecto Sepia:** Transformación lineal de color implementada mediante producto de matrices (operador `@`) utilizando los coeficientes estándar de Microsoft.
* **Visualización Interactiva:** Comparación lado a lado de la imagen original vs. la procesada mediante Matplotlib con soporte para imágenes 2D y 3D, y cierre automático mediante eventos de teclado (`key_press_event`).
* **Manejo de Archivos y Menú:** Carga y guardado seguro de imágenes con control de excepciones y estructura interactiva modular en bucle `while`.

---

## 🛠️ Requisitos e Instalación

Asegúrate de tener Python 3.8 o superior instalado. Instala las dependencias necesarias mediante `pip`:

```bash
pip install numpy pillow matplotlib

```

---

## 🚀 Uso de la Aplicación

1. Clona este repositorio o descarga los archivos en tu equipo:
```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO

```


2. Coloca la imagen que desees procesar en el directorio raíz del proyecto (por defecto el script busca `cara1.png`).
3. Ejecuta la aplicación desde la terminal:
```bash
python main.py

```


4. Utiliza las opciones del menú numérico para seleccionar la transformación a aplicar. Tras la ejecución de cada filtro, se desplegará una ventana interactiva mostrando el resultado; presiona cualquier tecla para cerrar la visualización y regresar al menú.

---

## 📐 Fundamento Matemático de las Transformaciones

### 1. Escala de Grises

$$I_{\text{gris}}(x, y) = \frac{R(x, y) + G(x, y) + B(x, y)}{3}$$

### 2. Contraste

$$I_{\text{contraste}}(x, y) = \text{clip}\Big( \alpha \cdot \big(I_{\text{float}}(x, y) - 128.0\big) + 128.0, \, 0, \, 255 \Big)$$

### 3. Transformación Sepia (Producto Matricial)

$$\begin{bmatrix} R' & G' & B' \end{bmatrix} = \begin{bmatrix} R & G & B \end{bmatrix} \begin{bmatrix} 0.393 & 0.349 & 0.272 \\ 0.769 & 0.686 & 0.534 \\ 0.189 & 0.168 & 0.131 \end{bmatrix}$$

---

## 📂 Estructura del Proyecto

```text
.
├── main.py            # Script principal con el menú, la lógica de filtros y la interfaz gráfica
├── cara1.png          # Imagen de prueba de entrada
├── README.md          # Documentación del proyecto
└── .gitignore         # Configuración para la exclusión de archivos temporales e imágenes generadas

```

---