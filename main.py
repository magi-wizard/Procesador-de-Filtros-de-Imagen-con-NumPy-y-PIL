from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#presenta el menu en la consola
def pinta_menu():
    print("*" * 30)
    print("Menu filtros de imagen")
    print("*" * 30)
    print("1.- Convierte la imagen a escala de grises.")
    print("2.- Crea un negativo de la imagen.")
    print("3.- Cambia el brillo de la imagen")
    print("4.- Cambia el contraste de la imagen")
    print("5.- Cambia el color a sepia")
    print("6.- Salir")

#carga la imagen del fichero
def carga_imagen(img_file:str):
    try:
        with Image.open(img_file).convert("RGB") as imagen:
            imagen.load()
    except FileNotFoundError as e:
        print(f"Error, el fichero {img_file} no existe.")
    except Exception as e:
        print(f"Error, ocurrió un error inesperado {e.__class__.__name__}")
    else:
        img_rgb = np.array(imagen)
        print(img_rgb.shape)
        return img_rgb

#convierte una imagen en escala de grises
def convertir_grises(img_rgb: np.ndarray):
    img_dst = img_rgb.mean(axis=2).astype(np.uint8)
    return img_dst

#Convierte la imagen en su negativo
def convertir_negativo(img_rgb:np.ndarray):
    img_dst = 255 - img_rgb
    return img_dst

#Aumenta o disminuye el brillo de la imagen
def cambiar_brillo(img_rgb: np.ndarray, brillo=40):
    img_dst = np.clip(img_rgb.astype(np.int16) + brillo, 0, 255).astype(np.uint8)
    return  img_dst

#Aumenta o disminuye el contraste de la imagen
def cambiar_contraste(img_rgb:np.ndarray, factor= 1.3):
    img_float = img_rgb.astype(np.float32)
    #Cálculo que aplica el contraste a la imagen
    img_dst = factor * (img_float -128.0) + 128.0
    img_dst = np.clip(img_dst, 0, 255).astype(np.uint8)
    return img_dst

#Convierte la imagen a tonos sepia
def convertir_sepia(img_rgb:np.ndarray):
    # Matriz de transformación sepia, corresponden con el estándar de Microsoft
    matriz_sepia = np.array([
        [0.393, 0.349, 0.272],
        [0.769, 0.686, 0.534],
        [0.189, 0.168, 0.131]])
    #Multiplicación matricial a lo largo deñ último eje (canales RGB)
    img_dst = img_rgb @ matriz_sepia
    img_dst = np.clip(img_dst, 0, 255).astype(np.uint8)
    return img_dst

#Guarda la imagen en un fichero
def guarda_imagen(img_rgb:np.ndarray, nombre_fichero:str):
    imagen = Image.fromarray(img_rgb)
    imagen.save(nombre_fichero)

def mostrar_comparativa(img_1: np.ndarray, img_2: np.ndarray, titulo_filtro):
    # Crear figura con 1 fila 2 columnas
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Mostrar imagen original en el primer panel
    axes[0].imshow(img_1)
    axes[0].set_title('Original')
    axes[0].axis('off')

    # Mostrar imagen filtrada en el segundo panel
    # Validar si la imagen es 2D (grises) o 3B (RGB)
    if img_2.ndim == 2:
        axes[1].imshow(img_2, cmap='gray')
    else:
        axes[1].imshow(img_2)

    axes[1].set_title(titulo_filtro)
    axes[1].axis('off')

    # Ajustar diseño  mostrarlo
    plt.tight_layout()
    plt.show()

def main():

    img_rgb = carga_imagen("cara1.png")

    while True:
        pinta_menu()

        entrada = input("Introduce una opción: ")

        if entrada == '6':
            break

        if entrada == '1':
            #convierte la imagen
            img_filtro = convertir_grises(img_rgb)
            guarda_imagen(img_filtro, "img_grises.jpg")
            mostrar_comparativa(img_rgb, img_filtro, 'Escala de grises')
        elif entrada == '2':
            img_filtro = convertir_negativo(img_rgb)
            guarda_imagen(img_filtro, "img_negativo.jpg")
            mostrar_comparativa(img_rgb, img_filtro, 'Negativo')
        elif entrada == '3':
            while True:
                try:
                    brillo = int(input("introduce un valor positivo para aumentar, uno negativo para disminuir: "))
                except ValueError:
                    print("El brillo introducido no es válido.")
                else:
                    img_filtro = cambiar_brillo(img_rgb, brillo)
                    break
            guarda_imagen(img_filtro, "img_brillo.jpg")
            mostrar_comparativa(img_rgb, img_filtro, 'Brillo')
        elif entrada == '4':
            while True:
                try:
                    contraste = float(input("introduce un valor decimal ejemplo: 1.5 para aumentar, 0.5 para disminuir: "))
                except ValueError:
                    print("El contraste introducido no es válido.")
                else:
                    img_filtro = cambiar_contraste(img_rgb, contraste)
                    break
            guarda_imagen(img_filtro, 'img_contraste.jpg')
            mostrar_comparativa(img_rgb, img_filtro, 'Contraste')
        elif entrada == '5':
            img_filtro = convertir_sepia(img_rgb)
            guarda_imagen(img_filtro, 'img_sepia.jpg')
            mostrar_comparativa(img_rgb, img_filtro, 'Sepia')
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()