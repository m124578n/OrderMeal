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
        // 把每個 todo 的 HTML 集合起來放到畫面上
        state.stores.map(store => Store(store)).join('')
    );
}

function Store({id, status, note}){
    return `
        <div class="group store">
            ${id} ${status} ${note}
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
    .then(function (myJosn){
        if (myJosn["status"] == 200){
            myJosn["stores"].forEach(store => {
                state.stores =
                    [...state.stores, {
                        id: store[0],
                        status: store[1],
                        note: store[2]
                    }]
                }
            );
            updateState(state)
        }
        else if (myJosn["status"] == 404){
            location.href = "/?timeout=1"
        }
    })
}
