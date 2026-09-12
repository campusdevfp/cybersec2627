/* Al imprimir (o exportar a PDF), abre los desplegables para que las
   soluciones y las pistas aparezcan en el papel. Después los deja como estaban. */
(function () {
  let cerrados = [];

  function abrirTodos() {
    cerrados = Array.from(document.querySelectorAll("details:not([open])"));
    cerrados.forEach(function (d) { d.open = true; });
  }

  function restaurar() {
    cerrados.forEach(function (d) { d.open = false; });
    cerrados = [];
  }

  window.addEventListener("beforeprint", abrirTodos);
  window.addEventListener("afterprint", restaurar);

  // Safari antiguo no dispara beforeprint: se usa matchMedia como respaldo
  if (window.matchMedia) {
    var mq = window.matchMedia("print");
    var handler = function (m) { (m.matches ? abrirTodos : restaurar)(); };
    if (mq.addEventListener) { mq.addEventListener("change", handler); }
    else if (mq.addListener) { mq.addListener(handler); }
  }
})();
