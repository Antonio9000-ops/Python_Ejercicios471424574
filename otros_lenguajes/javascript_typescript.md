# JavaScript y TypeScript

## Fundamentos web

JavaScript es el lenguaje principal para añadir interactividad a páginas web. Para aprovecharlo bien conviene dominar HTML, CSS, el modelo cliente-servidor, el ciclo de carga de una página y cómo el navegador interpreta y ejecuta los recursos.

## DOM

El DOM (Document Object Model) representa el documento HTML como un árbol de nodos. Con JavaScript se pueden seleccionar elementos, modificar contenido, cambiar estilos, escuchar eventos y crear interfaces dinámicas.

Temas clave:

- Selectores (`querySelector`, `querySelectorAll`).
- Manipulación de atributos, clases y estilos.
- Eventos (`click`, `submit`, `input`, `keydown`).
- Creación y eliminación de elementos.

## Async/await

`async` y `await` permiten escribir código asíncrono de forma más legible que con cadenas largas de promesas. Son esenciales para trabajar con APIs, temporizadores, lectura de archivos en Node.js y operaciones que dependen de respuestas externas.

Conceptos importantes:

- Promesas.
- Manejo de errores con `try`/`catch` en funciones asíncronas.
- Ejecución secuencial vs. paralela con `Promise.all`.

## Node.js

Node.js permite ejecutar JavaScript fuera del navegador. Se usa para crear servidores, herramientas de línea de comandos, APIs, scripts de automatización y aplicaciones de tiempo real.

Puntos recomendados:

- Módulos (`import`/`export` y CommonJS).
- Gestión de paquetes con npm.
- Servidores HTTP básicos.
- Acceso a archivos y variables de entorno.

## TypeScript

TypeScript añade tipado estático a JavaScript. Ayuda a detectar errores antes de ejecutar el programa, mejora el autocompletado y facilita el mantenimiento de proyectos grandes.

Temas clave:

- Tipos básicos y tipos personalizados.
- Interfaces y clases.
- Genéricos.
- Tipado de funciones, objetos y respuestas de APIs.
- Configuración con `tsconfig.json`.

## APIs

Las APIs permiten que una aplicación se comunique con otros servicios. En la web es frecuente consumir APIs REST o GraphQL desde el navegador o desde Node.js.

Aspectos a practicar:

- Peticiones HTTP con `fetch`.
- Métodos `GET`, `POST`, `PUT`, `PATCH` y `DELETE`.
- Códigos de estado HTTP.
- Autenticación con tokens.
- Validación y manejo de errores.

## Frameworks modernos

Los frameworks modernos ayudan a construir aplicaciones escalables con componentes, estado, rutas y herramientas de compilación.

Frameworks y herramientas comunes:

- React.
- Vue.
- Angular.
- Svelte.
- Next.js.
- Vite.
