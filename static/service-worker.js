const CACHE_NAME = 'comunicados-cache-v1';
const urlsToCache = [
  '/',
  '/static/manifest.json',
  '/static/icon-192.png',
  '/static/bootstrap.min.css',
];

// 🔁 Instalar Service Worker y cachear archivos
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
  );
});

// 📦 Responder con caché cuando sea posible
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((respuesta) => respuesta || fetch(event.request))
  );
});

// 🧹 Limpiar caché viejo al actualizar
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((nombres) => Promise.all(
      nombres.filter((nombre) => nombre !== CACHE_NAME)
             .map((nombre) => caches.delete(nombre))
    ))
  );
});
