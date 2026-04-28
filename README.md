# act-27-abr
Actividad corta para clase de DevOps.

## Sobre el Dockerfile
Se utilizó como imagen básica python:3.9, debido a que queremos ejecutar una aplicación que corra en esa versión específica de Python.

Docker ayuda a resolver el problema de consistencia del caso debido a que, al contenedorizar, la aplicación se corre con los requerimientos especificados en el Dockerfile, sin que se presenten problemas de dependencias al correrse en distintas máquinas.

Esa es la mayor ventaja de utilizar Docker: Es mucho más rápido y menos molesto que diseñar aplicaciones para varios tipos de máquinas (y probar todas esas versiones), debido a que un contenedor correrá en cualquier lado, lo cual significa que, al utilizar Docker, hay que crear una sola aplicación y probarla en una sola máquina.
