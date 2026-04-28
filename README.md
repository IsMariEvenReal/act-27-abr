# act-27-abr
Actividad corta para clase de DevOps.

## Sobre el Dockerfile
Se utilizó como imagen básica python:3.9, debido a que queremos ejecutar una aplicación que corra en esa versión específica de Python.

Docker ayuda a resolver el problema de consistencia del caso debido a que, al contenedorizar, la aplicación se corre con los requerimientos especificados en el Dockerfile, sin que se presenten problemas de dependencias al correrse en distintas máquinas.

Esa es la mayor ventaja de utilizar Docker: Es mucho más rápido y menos molesto que diseñar aplicaciones para varios tipos de máquinas (y probar todas esas versiones), debido a que un contenedor correrá en cualquier lado, lo cual significa que, al utilizar Docker, hay que crear una sola aplicación y probarla en una sola máquina.

## ¿Cómo se utiliza infraestructura.yaml?

El archivo infraestructura.yaml es una plantilla para CloudFormation; es decir, una especie de script de automatización que crea recursos automáticamente, como parte de lo que llamamos un stack.

Esta plantilla puede validarse y ejecutarse a través de AWS CLI o de la terminal de una instancia EC2 correctamente configurada, esto al ejecutar los siguientes dos comandos:

aws cloudformation validate-template --template-body file://infraestructura.yaml

aws cloudformation create-stack \
    --stack-name nombre-del-stack \
    --template-body file://infaestructura.yaml \
    --capabilities CAPABILITY IAM

## Pipeline CI/CD

Esta actividad incluye un pipeline CI/CD que, aunque no se ejecutará en AWS, debería ser funcional en GitHub Actions. Este pipeline incluye las etapas de source, build, test, deploy y monitoreo.

En la etapa Source, se recupera el código desde este mismo repo.

En la etapa Build, se construye el contenedor, que tendrá como nombre "mi-app" (en un pipeline en AWS, esto se haría en AWS CodeBuild).

En la etapa Test, se ejecuta Pytest. En una app real, Pytest ejecutaría pruebas unitarias, mas en este caso, para mantener simple el proyecto, solo hace un print que dice que se están ejecutando pruebas.

En la etapa Deploy, se echa a andar el contenedor (en AWS, utilizaríamos CodeDeploy para esto).

Y por último, en la etapa de monitoreo, se simula el envío de métricas a otra plataforma (que, en un pipeline ejecutado en AWS, sería CloudWatch).