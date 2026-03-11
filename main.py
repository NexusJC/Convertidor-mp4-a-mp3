from converter import convert_mp4_to_mp3
from utils import create_output_folder, get_output_name

def main():

    print("=== CONVERTIDOR MP4 → MP3 ===\n")

    create_output_folder()

    input_file = input("Ingresa la ruta del archivo MP4: ")

    output_file = get_output_name(input_file)

    success = convert_mp4_to_mp3(input_file, output_file)

    if success:
        print("\n Conversión completada")
        print("Archivo guardado en:", output_file)
    else:
        print("\n Error en la conversión")


if __name__ == "__main__":
    main()