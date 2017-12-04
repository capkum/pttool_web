document.addEventListener('DOMContentLoaded', () => {
    let target = document.querySelectorAll('.navbar-burger');
    let $navbarBurgers = Array.prototype.slice.call(target, 0);

    if ($navbarBurgers.length > 0) {
        $navbarBurgers.forEach($el => {
            $el.addEventListener('click', () => {

                let target = $el.dataset.target;
                let $target = document.getElementById(target);

                $el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        })
    }

});