import boto3
from datetime import datetime
from botocore.exceptions import ClientError

def generar_reporte():
    # Se inicializan los recursos de AWS
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    s3 = boto3.resource('s3')
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_archivo = "/home/ubuntu/reporte_recursos.txt"

    print(f"--- GENERANDO REPORTE DE EC2 y S3 PARA SOLUCIONES TECNOLÓGICAS DEL FUTURO ---")

    with open(nombre_archivo, "w") as f:
        f.write(f"REPORTE DE INFRAESTRUCTURA - {fecha_actual}\n")
        f.write("="*60 + "\n\n")

        # Reporte de instancias EC2
        f.write("--- INSTANCIAS EC2 ---\n")
        instancias = list(ec2.instances.all())
        #Se listan TODAS las instancias
        if not instancias:
            f.write("No hay instancias EC2 actualmente.\n")
        else:
            for inst in instancias:
                f.write(f"ID: {inst.id} | Estado: {inst.state['Name']} | Tipo: {inst.instance_type}\n")
        
        f.write("\n" + "-"*30 + "\n\n")

        # Reporte de buckets S3 y sus objetos
        f.write("--- INVENTARIO S3 ---\n")
        try:
            buckets = list(s3.buckets.all())
            #Se listan TODOS los buckets
            if not buckets:
                f.write("No se encontraron buckets S3.\n")
            else:
                for bucket in buckets:
                    f.write(f"BUCKET: {bucket.name}\n")
        except ClientError as e:
            f.write(f"ERROR ACCEDIENDO A S3\n")

        f.write("="*60 + "\n")
        f.write("FIN DEL REPORTE.")

    print(f"Reporte generado exitosamente: {nombre_archivo}")

if __name__ == "__main__":
    generar_reporte()