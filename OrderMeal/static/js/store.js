let state = {
    stores : [],
}

// 更新 state
function updateState(newState) {
    state = newState;
    render()
}
        
// state => UI
function render() {
    // 先把畫面清空
    $('.storeArea').empty();
    console.log(state)
    $('.storeArea').append(
        // 把每個 store 的 HTML 集合起來放到畫面上
        state.stores.map(store => Store(store)).join('')
    );
}

function Store({id, status, note, image_url}){
    return `
        <div class="group store">
            <img src="${image_url}" width="150px" height="120px" alt="" />
            ${id} ${status} ${note}
            <a href="/group/order?store=${id}" style="height:20px">開團</a>
        </div>
    `
}

function get_all_stores(){
    fetch("/api/store/", {
        headers: {
            "Authorization": "Bearer" + " " + localStorage.getItem('token'),
        },
        method: "GET",
    })
    .then(function (response){
        return response.json()
    })
    .then(function (myJson){
        if (myJson["status"] == 200){
            myJson["stores"].forEach(store => {
                state.stores =
                    [...state.stores, {
                        id: store[0],
                        status: store[1],
                        note: store[2],
                        image_url: null
                    }]
                }
            );
            updateState(state)
        }
        else if (myJson["status"] == 404){
            location.href = "/?timeout=1"
        }
        get_all_images()
    })
}

function get_all_images(){
    fetch("/api/store/images/", {
        headers: {
            "Authorization": "Bearer" + " " + localStorage.getItem('token'),
        },
        method: "GET",
    })
    .then(function (response){
        return response.json()
    })
    .then(function (myJson){
        console.log(myJson)
        if (myJson["status"] == 200){
            myJson["images"].forEach(image => {
                state.stores.map(store => {
                    if (store["id"] == image[0]){
                        store["image_url"] = image[1]
                        }
                    })
                }
            )
            updateState(state)
        }
        else if (myJson["status"] == 404){
            location.href = "/?timeout=1"
        }
    })
}
