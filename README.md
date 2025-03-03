# Image Background Removal Script

Este script en Python elimina el fondo de una imagen utilizando la librería `rembg`, y guarda el resultado en formato PNG con el fondo transparente.

## Requisitos

Para usar este script, asegúrate de tener Python instalado y las siguientes librerías:

- `rembg` - Para la eliminación del fondo.
- `PIL` (Pillow) - Para manipular imágenes.

Puedes instalar estas librerías ejecutando el siguiente comando:

    ```bash
    pip install rembg pillow


## Uso

- Coloca la imagen de entrada en el directorio de trabajo o especifica la ruta de la imagen en el código (reemplazando "root\\input_path.jpg" con la ruta correcta de tu imagen).
- Ejecuta el script.
- El fondo de la imagen será removido y el resultado será guardado en el archivo "root\\output_path.png". Puedes cambiar la ruta y el nombre del archivo de salida según lo necesites.
