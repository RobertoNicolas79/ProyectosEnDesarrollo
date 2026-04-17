const fila = document.querySelector('.contenedor-carousel');
const peliculas= document.querySelectorAll('.pelicula');

const flechaizquierda = document.getElementById('flecha-izquierda');
const flechaderecha = document.getElementById('flecha-derecha');



//-----------------Event listener para flecha derecha---------//

flechaderecha.addEventListener('click', () => {
    fila.scrollLeft += fila.offsetWidth;

    const indicadorActivo = document.querySelector('.indicadores .activo');
    if(indicadorActivo.nextElementSibling){
        indicadorActivo.nextElementSibling.classList.add('activo')
        indicadorActivo.classList.remove('activo');

    }
});


//-----------------Event listener para flecha izqueirda---------//
flechaizquierda.addEventListener('click', () => {
    fila.scrollLeft -= fila.offsetWidth;

    const indicadorActivo = document.querySelector('.indicadores .activo');
    if(indicadorActivo.previousElementSibling){
        indicadorActivo.previousElementSibling.classList.add('activo')
        indicadorActivo.classList.remove('activo');

    }
});

//-----------------Event listener para paginacion---------//

const numeroPaginas= Math.ceil(peliculas.length / 5);

for(let i = 0; i < numeroPaginas; i++){
    const indicador = document.createElement('button');

    if (i===0){
        indicador.classList.add('activo');

    }

    document.querySelector('.indicadores').appendChild(indicador);

    indicador.addEventListener('click', (e) =>{
        fila.scrollLeft = i * fila.offsetWidth;
    

    document.querySelector('.indicadores .activo').classList.remove('activo');
    e.target.classList.add('activo');
    });
}


//-----------------hover---------//

peliculas.forEach((pelicula) => {
    pelicula.addEventListener('mouseenter', (e) =>{
       const elemento = e.currentTarget;
       setTimeout(() =>{
           peliculas.forEach(pelicula => pelicula.classList.remove('hover'));
           elemento.classList.add('hover');
       }, 50) ;
    })

});

fila.addEventListener('mouseleave', () =>{
    peliculas.forEach(pelicula => pelicula.classList.remove('hover'));
})
peliculas.forEach((pelicula) =>{
    pelicula.addEventListener('click', (a) =>{
        const nose = a.currentTarget;
        setTimeout(() =>{
         peliculas.forEach(pelicula => pelicula.classList.remove('active'))
            nose.classList.add('active');
        })
    })
})