const btnsEliminar = this.document.querySelectorAll('.btnEliminacion');

(function (){
    btnsEliminar.forEach(btn => {
        console.log(btn)
        btn.addEventListener('click', function(e){
            let confirmar = confirm('Este transformador se eliminará');
            if (!confirmar){
                e.preventDefault();
            }
        })
    })
})();