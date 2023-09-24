let dataTable;
let dataTableIsInitialized = false;

const initDatatable = async()=>{
    if (dataTableIsInitialized){
        dataTable.destroy();
    }

    await listbecas();

    dataTable = $("#datatable-becas").DataTable();

    dataTableIsInitialized = true;
}


const listbecas = async () => {
  try {
    const response = await fetch("http://127.0.0.1:8000/list_becas");
    const data = await response.json();
    let content = "";

    data.Becas.forEach((Beca, index) => {
      content += `
        <tr>
            <td>${index}</td>
            <td>${Beca.nombre}</td>
            <td>${Beca.tipo}</td>
            <td>${Beca.monto}</td>
        </tr>
        `;
    });
    tablebody_becas.innerHTML = content;
  } catch (ex) {
    alert(ex);
  }
};

window.addEventListener("load", async () => {
  await initDatatable();
});
