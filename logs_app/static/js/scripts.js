const container = document.querySelector('.log-container');

//  Obtener búsqueda desde HTML
const search = document.body.dataset.search.toLowerCase();

//  Highlight dinámico
if (search) {
    document.querySelectorAll('.log-container div').forEach(el => {
        const text = el.innerHTML;
        const regex = new RegExp(search, "gi");
        el.innerHTML = text.replace(regex, match => `<mark>${match}</mark>`);
    });
}
