var range = document.getElementById("range").addEventListener('input', printValueRange)
var label_range = document.getElementById("label-range")

function printValueRange(){
    data = document.getElementById("range").value

    label_range.innerHTML = data + "%";
}

function edit(element){
    var data = element.parentNode.parentNode 

    // get data from table edit
    var order = data.querySelector("#order").value
    var artist = data.querySelector("#artist").value
    var album = data.querySelector("#album").value
    var track = data.querySelector("#track").value
    var time = data.querySelector("#time").value


    // modal edit
    var modal_edit = document.getElementById("modal-edit")
    

    //set data in table modal
    
    modal_edit.querySelector("#order-edit").value = order
    modal_edit.querySelector("#artist-edit").value = artist
    modal_edit.querySelector("#album-edit").value = album
    modal_edit.querySelector("#track-edit").value = track
    modal_edit.querySelector("#time-edit").value = time
    
    modal_edit.querySelector("#title-modal").innerText = order + " - " + track
}   

function info_public(element){
    console.log()
    var track = element.parentNode.parentNode.childNodes[7].innerText


    var modalInfo = document.getElementById('exampleModalLabel')
    modalInfo.innerText = track

    //console.log(element.parentNode.parentNode.parentNode.getElementsByClassName('data_track')[0].value)
    var data = element.parentNode.parentNode.getElementsByClassName('data_track')[0].value
    
    // var data = element.parentNode.parentNode.getElementsByClassName('data_track')[0].value

    if (data){

        console.log("verdadero")
        var data_format = data.split("\'").join("\"")

        var data_json = JSON.parse(data_format)
    
        //console.log(element.parentNode.parentNode.getElementsByClassName('data_track')[0].value)
    
    
        document.getElementById("url-youtube").href = data_json.youtube
        document.getElementById("url-guitar-1").href = data_json.tab_guitar_1
        document.getElementById("url-guitar-2").href = data_json.tab_guitar_2
        document.getElementById("url-bass").href = data_json.tab_bass
        document.getElementById("url-link-1").href = data_json.link_1
        document.getElementById("url-link-2").href = data_json.link_2
        document.getElementById("url-link-3").href = data_json.link_3

    }else{
        console.log("falso")

        document.getElementById("url-youtube").href = ""
        document.getElementById("url-guitar-1").href = ""
        document.getElementById("url-guitar-2").href = ""
        document.getElementById("url-bass").href = ""
        document.getElementById("url-link-1").href = ""
        document.getElementById("url-link-2").href = ""
        document.getElementById("url-link-3").href = ""
    }




    

}


function info(element){
    var order = element.parentNode.parentNode.firstElementChild.childNodes[0]
    order = order.value

    var track = element.parentNode.parentNode.childNodes[9].childNodes[0]
    track = track.value

    var modalInfo = document.getElementById('exampleModalLabel')
    modalInfo.innerText = track

    var orderModal = document.getElementById('track-order')
    orderModal.value = order

    var data = element.parentNode.parentNode.getElementsByClassName('data_track')[0].value

    var data_format = data.split("\'").join("\"")

    var data_json = JSON.parse(data_format)


    document.getElementById("url-youtube").value = data_json.youtube
    document.getElementById("url-guitar-1").value = data_json.tab_guitar_1
    document.getElementById("url-guitar-2").value = data_json.tab_guitar_2
    document.getElementById("url-bass").value = data_json.tab_bass
    document.getElementById("url-link-1").value = data_json.link_1
    document.getElementById("url-link-2").value = data_json.link_2
    document.getElementById("url-link-3").value = data_json.link_3
}


function pop(element){
    var table = document.getElementById("table")
    
    index=element.parentNode.parentNode.cells[0].innerText
    element.parentNode.parentNode.remove()
    console.log("index: " + index)
    for (var i = index; i < table.rows.length; i++){
        table.rows[i].cells[0].innerHTML = "<input type='hidden' name='order' value="+ i +">" + i
        console.log( table.rows[i] )
    }
}

// ? view_list.html modal 
function deletelist(value){
    console.log(value)
    var list_name = document.getElementById("list_name")
    var btn_delete = document.getElementById("btn-delete")
    list_name.innerHTML = '<label for="">' + value +  '</label>'
    btn_delete.value = value
}

var index;  // variable to set the selected row indexs
var table_len;
function getSelectedRow()
{
    var table = document.getElementById("table");
    table_len = table.rows.length

    for(var i = 1; i < table.rows.length; i++)
    {
        table.rows[i].onclick = function()
        {
            // clear the selected from the previous selected row
            // the first time index is undefined
            if(typeof index !== "undefined"){
                table.rows[index].classList.toggle("table-dark");
                
            }
            
            index = this.rowIndex;
            
            this.classList.toggle("table-dark");

        };
    }
        
}

getSelectedRow();

function changeNumer(direction, element){
    if (direction === "up"){
        var num = this.index - 1;
            
        if (num > 0){
            // ? element[this.index].cells[0].innerText = num.toString();
            element[this.index].cells[0].innerHTML = '<input type="hidden" name="order" value='+ num.toString() +'>' + num.toString()
            
            num = this.index;
            // ? element[this.index - 1].cells[0].innerText = num.toString(); 
            element[this.index - 1].cells[0].innerHTML = '<input type="hidden" name="order" value='+ num.toString() +'>' + num.toString()
            
        }
    }
    
    if (direction === "down"){
        var num = this.index + 1;

        if (num < table_len){
            // ? element[this.index].cells[0].innerText = num.toString();
            element[this.index].cells[0].innerHTML = '<input type="hidden" name="order" value='+ num.toString() +'>' + num.toString()
            
            num = this.index;
            // ? element[this.index + 1].cells[0].innerText = num.toString(); 
            element[this.index + 1].cells[0].innerHTML = '<input type="hidden" name="order" value='+ num.toString() +'>' + num.toString()
            
            
        }

    }
}


function upNdown(direction)
{
    //console.log("upNdown: ",index)
    var rows = document.getElementById("table").rows,
        parent = rows[index].parentNode;
        
        if(direction === "up"){
        
            // var num = this.index - 1;
            // if (num > 0){
            //     rows[this.index].cells[0].innerText = num.toString();
            //     num = this.index;
            //     rows[this.index - 1].cells[0].innerText = num.toString();
            // } 
            
            changeNumer("up",rows)
    
        if(index > 1){
            parent.insertBefore(rows[index],rows[index - 1]);
            // when the row go up the index will be equal to index - 1

            index--;
        }
    }
    
    if(direction === "down"){
        
        // var num = this.index + 1
        // if (num < table_len){
        //     rows[this.index].cells[0].innerText = num.toString()
        //     num = this.index;
        //     rows[this.index + 1].cells[0].innerText = num.toString();
        // }

        changeNumer("down",rows)

        if(index < rows.length - 1){
            parent.insertBefore(rows[index + 1],rows[index]);
            // when the row go down the index will be equal to index + 1
            
            index++;
        }
    }
}