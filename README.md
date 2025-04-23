# Arquitectura

### Cliente (Usuario):
>El cliente (puede ser una aplicación web o móvil) se comunica con el Backend a través de WebSockets.
Enviará datos en tiempo real (como video o imágenes del lenguaje de señas) y recibirá la traducción (texto o audio).
### Backend:

>El Backend recibe los datos de lenguaje de señas del cliente a través de WebSockets.
Luego, el backend puede comunicarse con otros microservicios (por ejemplo, para traducir el lenguaje de señas) usando gRPC (para alta eficiencia) o REST (si no se requiere baja latencia).
El backend procesará la información y devolverá la traducción al usuario a través de WebSockets.
### Microservicios:
>Los microservicios internos pueden encargarse de tareas específicas, como procesar imágenes de lenguaje de señas y devolver el resultado al backend. 
La comunicación entre estos microservicios puede ser realizada utilizando gRPC si la latencia es una preocupación o REST si la simplicidad es más importante.
Editor Markdown es un editor online que se ejecuta en tu navegador y que funciona tanto con tus archivos locales como con varios servicios de almacenamiento cloud.
```
/backend                           # Raíz del proyecto backend
│
├── /java                           # Microservicio en Java
│   ├── /src                        # Código fuente de Java
│   │   ├── /main
│   │   │   ├── /java               # Clases Java
│   │   │   │   ├── /controller     # Controladores Java (API)
│   │   │   │   │   └── SignLanguageController.java   # Controlador para lenguaje de señas
│   │   │   │   ├── /service        # Servicios Java (Lógica de negocio)
│   │   │   │   │   └── SignLanguageService.java      # Servicio de procesamiento de lenguaje de señas
│   │   │   │   ├── /model          # Entidades Java
│   │   │   │   │   └── SignLanguage.java            # Modelo para lenguaje de señas
│   │   │   │   ├── /dto            # DTOs en Java
│   │   │   │   │   └── SignLanguageDto.java         # DTO para lenguaje de señas
│   │   │   │   ├── /repository     # Repositorios Java (Acceso a datos)
│   │   │   │   │   └── SignLanguageRepository.java   # Repositorio para operaciones de DB
│   │   │   │   └── /config         # Archivos de configuración de Spring Boot (Java)
│   │   │   │       └── application.yml                 # Configuración de la aplicación en Java
│   │   │   │       └── grpc-config.yml                 # Configuración de gRPC para Java
│   │   │   │       └── gateway-config.yml              # Configuración del API Gateway en Java
│   │   │   │       └── application.properties          # Configuración de propiedades Java
│   ├── /target                     # Archivos generados por la compilación (Java)
│   ├── /Dockerfile                 # Dockerfile para microservicio en Java
│   ├── /pom.xml                   # Archivo de dependencias de Maven (Java)
│
├── /python                         # Microservicio en Python
│   ├── /app                         # Código fuente de Python
│   │   ├── /controllers             # Controladores Python
│   │   │   └── sign_language_controller.py # Controlador para lenguaje de señas
│   │   ├── /services                # Servicios Python
│   │   │   └── sign_language_service.py  # Servicio de procesamiento de lenguaje de señas
│   │   ├── /models                  # Modelos en Python
│   │   │   └── sign_language.py         # Modelo para lenguaje de señas
│   │   ├── /dto                     # DTOs en Python
│   │   │   └── sign_language_dto.py  # DTO para lenguaje de señas
│   │   ├── /repository              # Repositorios Python (Acceso a datos)
│   │   │   └── sign_language_repository.py  # Repositorio para operaciones de DB
│   │   ├── /config                  # Archivos de configuración para Python
│   │   │   └── application.yml       # Configuración de la aplicación en Python
│   │   │   └── grpc-config.yml       # Configuración de gRPC para Python
│   │   │   └── gateway-config.yml    # Configuración del API Gateway para Python
│   ├── /requirements.txt           # Requisitos de dependencias para Python
│   ├── /Dockerfile                 # Dockerfile para microservicio en Python
│   ├── /run.py                     # Script para ejecutar la aplicación Python
│   ├── /setup.py                   # Archivo de configuración de instalación para Python
│
├── /gateway                        # API Gateway
│   ├── /src                         # Código fuente del Gateway
│   │   ├── /controller              # Controladores del Gateway
│   │   │   ├── SignLanguageGatewayController.java  # Controlador para manejar solicitudes de lenguaje de señas
│   │   ├── /config                  # Configuración del Gateway
│   │   │   ├── application.yml      # Configuración del API Gateway
│   │   │   ├── routing-config.yml   # Configuración de las rutas del API Gateway
│   ├── /Dockerfile                  # Dockerfile para el API Gateway
│   ├── /pom.xml                    # Archivo de dependencias del Gateway
│
├── /common                         # Librerías y utilidades comunes entre servicios (Java/Python)
│   ├── /java                       # Utilidades comunes para microservicios Java
│   │   ├── /utils                  # Funciones comunes en Java
│   │   │   └── Utils.java          # Funciones comunes en Java
│   │   ├── /exceptions             # Excepciones personalizadas para Java
│   │   │   └── CustomException.java # Excepción en Java
│   │   ├── /config                 # Archivos de configuración comunes para Java
│   │   │   └── application.yml     # Configuración de la aplicación en Java
│   │   │   └── grpc-config.yml     # Configuración de gRPC para Java
│   │   │   └── gateway-config.yml  # Configuración del API Gateway para Java
│   │   ├── /dto                    # DTOs comunes para Java
│   │   │   └── SignLanguageDto.java # DTO para lenguaje de señas en Java
│   │
│   ├── /python                     # Utilidades comunes para microservicios Python
│   │   ├── /utils                  # Funciones comunes en Python
│   │   │   └── utils.py            # Funciones comunes en Python
│   │   ├── /exceptions             # Excepciones personalizadas para Python
│   │   │   └── custom_exception.py # Excepción en Python
│   │   ├── /config                 # Archivos de configuración comunes para Python
│   │   │   └── application.yml     # Configuración de la aplicación en Python
│   │   │   └── grpc-config.yml     # Configuración de gRPC para Python
│   │   │   └── gateway-config.yml  # Configuración del API Gateway para Python
│   │   ├── /dto                    # DTOs comunes para Python
│   │   │   └── sign_language_dto.py # DTO para lenguaje de señas en Python
│
├── /docker                         # Archivos relacionados con Docker
│   ├── /java                       # Configuración Docker para Java
│   └── /python                     # Configuración Docker para Python
│
├── /k8s                            # Archivos de configuración para Kubernetes
│   ├── /java                       # Configuración Kubernetes para Java
│   └── /python                     # Configuración Kubernetes para Python
└── /README.md                      # Documentación del proyecto
```
---

## 🚀 Tecnologías Utilizadas

| Componente | Tecnología |
|-----------|------------|
| Microservicios (Java) | Spring Boot, Maven, JPA |
| Microservicios (Python) | Flask o FastAPI |
| Comunicación | REST, gRPC |
| Gateway | Spring Cloud Gateway |
| Contenedores | Docker |
| Orquestación | Kubernetes (opcional) |


## 🔌 Comunicación entre servicios

| Servicio | Tecnología | Comunicación |
|----------|----------|----------|
| sign-vision-ai (Python)    | **gRPC**   | Envia frames de video capturados en tiempo real   |
| audio-synthesis (Python)    | **gRPC**   | Recibe texto y devuelve audio   |
| sign-language-api (Java)    | **REST**   | Interactúa con frontend   |
| audio-text-api (Java)    | **REST**  | Traduce audio a texto   |
| gateway (Java)    | **REST**  | Redirige solicitudes al servicio correspondiente  |

## 🔗 Comunicación Entre Servicios

- **gRPC**: Comunicación eficiente entre microservicios internos (Java y Python).
- **REST**: Interfaces externas a través del API Gateway.

## 📦 API Gateway

- Rutea y orquesta las solicitudes hacia los servicios Java y Python.
- Maneja la autenticación y la configuración centralizada.
- Define reglas de enrutamiento en `routing-config.yml`.

## 📚 Directorio `common/`

Contiene lógica y configuración compartida entre microservicios:

- DTOs
- Excepciones
- Utilidades comunes
- Archivos de configuración para gRPC y el Gateway

## 🧪 Testing

- Unit Testing: JUnit 5 / PyTest
- Integration Testing: TestContainers
- Contract Testing: gRPC and REST mocks
- API Testing: Insomnia/Postman

## 🔐 Seguridad

- Autenticación JWT (Spring Security)
- Validación de payloads
- Control de acceso por roles en gateway

## 🐳 Despliegue

1. **Construir imágenes Docker**:
   ```bash
   docker build -t java-service ./java
   docker build -t python-service ./python
   docker build -t api-gateway ./gateway

---

# 🛍️ Guía de Colaboración para Desarrolladores

## 🛡 Estructura de Ramas

- **`main`**: Rama principal. Contiene solo código **estable y listo para producción**.
- **`develop`**: Rama de desarrollo. Aquí se integran nuevas funcionalidades antes de pasar a producción.

---

## 🔐 Reglas Generales

- ❌ No se permite hacer `push` directo a `main`.
- ✅ Todo el desarrollo se hace desde una rama creada a partir de `develop`.
- 📩 Los Pull Requests se hacen **siempre hacia `develop`**.
- 🔍 Solo el responsable del proyecto fusiona `develop` con `main` una vez revisado todo.

---

## 🔁 Flujo de Trabajo

### 1. 📥 Obtener la última versión de `develop`

```bash
git checkout develop
git pull origin develop
```

---

### 2. 🌿 Crear una nueva rama para tu funcionalidad

```bash
git checkout -b nombre-de-la-rama
```

> 📝 Usa nombres descriptivos para la rama según la funcionalidad que vas a trabajar.

#### Ejemplos de nombres de ramas:

| Funcionalidad       | Nombre de la rama        |
|---------------------|--------------------------|
| Clase Usuario        | `usuario`                |
| Vista de login       | `login-ui`               |
| Validación de tokens | `token-validation`       |
| Mejoras al README    | `mejoras-readme`         |

---

### 3. 👨‍💼 Trabaja en tu funcionalidad

```bash
git add .
git commit -m "Agrega clase Usuario con validaciones básicas"
```

---

### 4. 🚀 Sube tu rama al repositorio

```bash
git push -u origin nombre-de-la-rama
```

---

### 5. 📩 Crear un Pull Request hacia `develop`

1. Ve a GitHub
2. Crea un Pull Request de tu rama → `develop`
3. Espera revisión y aprobación
4. Resuelve conflictos si los hay (en tu rama)

---

### 6. ✅ Fusión final a `main`

El responsable del proyecto revisará y aprobará la integración de `develop` a `main` cuando todo esté verificado.

---

## 📌 Buenas Prácticas

- Haz commits pequeños y descriptivos.
- Actualiza tu rama frecuentemente con los últimos cambios de `develop`:
  ```bash
  git checkout develop
  git pull origin develop
  git checkout mi-rama
  git merge develop
  ```
- Borra tu rama local y remota una vez fusionada.

---

👥 Esta guía ayuda a mantener el proyecto ordenado y colaborativo.


