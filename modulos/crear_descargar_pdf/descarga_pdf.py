from tkinter import filedialog
import shutil

def descargar_pdf(nombre_archivo):
    # Lógica para guardar el PDF aquí
    ruta_archivo = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                filetypes=[("PDF files", "*.pdf")],
                                                initialfile="matricula_"+nombre_archivo
                                            )
    if ruta_archivo:
        archivo_existente = "matricula_pdf_img/pdf/matricula_"+nombre_archivo+".pdf"
        shutil.copy(archivo_existente, ruta_archivo)
        print(f"Archivo copiado a: {ruta_archivo}")
    else:
        print("No se seleccionó ninguna ubicación para guardar el PDF.")