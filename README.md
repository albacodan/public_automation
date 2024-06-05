# INVENTARIO

|   |   | 
|---|---|
| Nombre de la carpeta de trabajo | TFG-DAA |
| URL git | https://github.com/albacodan/public_automation |
| Version del desarrollo | 1.0  |
| Frecuencia de ejecucion | On Demand |
| Autor(es) del desarrollo  | danielalbarranacosta610@institutodh.net |
| Revisor(es) del desarrollo | danielalbarranacosta610@institutodh.net |
| Beneficiario(s) | Clientes |
| Criticidad (Alta, Media, Baja) | Media |
| Soporte (24x7, 8x5) | 8x5 |
| Fecha de ultima actualizacion | 04/06/2024 |
 
# CONTEXTO
Necesidad de creacion de diferentes automatismos para diferentes clientes. Estos automatismos de ejemplo consiste en creacion y eliminacion de grupos y usuarios, despliegue de contenedores docker de forma automatica, eliminacion de contenedores y docker, y como control de seguridad tenemos un envio via mail con informacion de los usuarios y privilegios.
  
# DESCRIPCION
Se realiza diferentes automatismos para satisfacer la necesidad de un instituto, el cual necesita agilizar tareas para su aulaTIC. Este instituto necesita crear un usuario para cada uno de los equipos, tanto alumnos como profesor, con su grupo correspondiente. Se ve la necesidad de desplegar contenedores en docker de forma automatica para el uso de los mismos, sobre todo Wordpress para realizar practicas de diseño web. Como mejora a nivel de controles de seguridad se implementa un automatismo que genera informes sobre los usuarios locales de cada maquina y sus privilegios. Por ultimo se desea que al terminar el curso sea posible eliminar todo lo desplegado.

# ACTUALIZACIONES
Se contempla la necesidad de que para un futuro se implementen nuevos automatismos en desarrollo (Carpeta Futuras Mejoras)

# INFORMACION ADICIONAL
Implementamos las notificaciones de los estado de ejecucion de los pipelines a un chat de Microsoft Teams. De forma que se podrá estar al tanto del estado y el numero de ejecuciones realizados.

Tambien se implementa en Jenkins un sistema de roles para los usuarios, de modo que es posible dividir los permisos de lectura y ejecucion de los propios pipelines para grupos de usuario.


