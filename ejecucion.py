import rpy2.robjects as robjects 
from datetime import date

def generar_reporte(project_path, rmd_file, output_dir):
    """Esta funcion compila el archivo `rmd_file` y guarda el reporte HTML en el directorio `output_dir`"""

    rcode = '''
setwd("{}")
Sys.setenv(RSTUDIO_PANDOC = "/usr/lib/rstudio-server/bin/pandoc")
rmarkdown::render("{}", output_dir = "{}")
    '''.format(project_path,rmd_file, output_dir)
    robjects.r(rcode)
    print("Reporte generado exitosamente!")
    print("Fecha:", str(date.today()))


generar_reporte(
    project_path = "/home/nombre_usuario/ProyectoSEE/Mini_Curso_Python_R_MYSQL/",
    rmd_file = "analisis.Rmd",
    output_dir = "reportes_produccion/" + str(date.today()) + "/"
)