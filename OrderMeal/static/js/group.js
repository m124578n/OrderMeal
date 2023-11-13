
let state = {
    START : [],
    END : [],
    own : []
}

// 更新 state
function updateState(newState, status) {
    state = newState;
    render(status)
}
        
// state => UI
function render(status) {
    // 先把畫面清空
    $('.groupArea'+"_"+status).empty();
    console.log(state, status)
    $('.groupArea'+"_"+status).append(
        // 把每個 todo 的 HTML 集合起來放到畫面上
        state[status].map(group => Group(group)).join('')
    );
}

function Group({id, status, note, store_id, image_url}){
    return `
        <div class="group">
            <img src="${image_url}" width="150px" height="120px" alt="" />
            ${id} ${status} ${store_id} ${note}
        </div>
    `
}


function get_all_groups_by_status(status){
    fetch("/api/group?status="+status, {
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
            myJosn["groups"].forEach(group => {
                state[status] =
                    [...state[status], {
                        id: group[0],
                        status: group[1],
                        note: group[2],
                        store_id: group[3],
                        image_url: null
                    }]
                }
            );
            updateState(state, status)
            get_all_images(status)
        }
        else if (myJosn["status"] == 404){
            location.href = "/?timeout=1"
        }
    })
}

function get_groups_by_user_id(){
    fetch("/api/group/user/", {
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
            myJosn["groups"].forEach(group => {
                state.own =
                    [...state.own, {
                        id: group[0],
                        status: group[1],
                        note: group[2],
                        store_id: group[3],
                        image_url: null
                    }]
                }
            );
            updateState(state, "own")
            get_all_images("own")
        }
        else if (myJosn["status"] == 404){
            location.href = "/?timeout=1"
        }
    })
}

function get_all_images(status){
    fetch("/api/store/images/", {
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
            myJosn["images"].forEach(image => {
                state[status].map(store => {
                    if (store["store_id"] == image[0]){
                        store["image_url"] = image[1]
                        }
                    })
                }
            )
            updateState(state, status)
        }
        else if (myJosn["status"] == 404){
            location.href = "/?timeout=1"
        }
    })
}
