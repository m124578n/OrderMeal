
let state = {
    groups : [],
    groups_end : [],
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
    if (status == "START"){
        $('.groupArea'+"_"+status).append(
            // 把每個 todo 的 HTML 集合起來放到畫面上
            state.groups.map(group => Group(group)).join('')
        );
    }
    else{
        $('.groupArea'+"_"+status).append(
            // 把每個 todo 的 HTML 集合起來放到畫面上
            state.groups_end.map(group => Group(group)).join('')
        );
    }
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
                if (status === "START"){
                    state.groups =
                        [...state.groups, {
                            id: group.id,
                            status: group.status,
                            note: group.note
                        }]
                    }
                if (status === "END"){
                    state.groups_end = [...state.groups_end, {
                            id: group.id,
                            status: group.status,
                            note: group.note
                        }]
                    }
                }
            );
            updateState(state, status)
        }
        else{
            alert(myJosn["status"])
        }
    })
}

function Group({id, status, note}){
    return `
        <div class="group">
            ${id} ${status} ${note}
        </div>
    `
}
