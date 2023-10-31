
let state = {
    groups : []
}

// 更新 state
function updateState(newState) {
    state = newState;
    render()
}
        
// state => UI
function render() {
    // 先把畫面清空
    $('.groupArea').empty();
    console.log(state.groups)
    $('.groupArea').append(
    // 把每個 todo 的 HTML 集合起來放到畫面上
    state.groups.map(group => Group(group)).join('')
    );
}

window.onload = get_all_groups;

function get_all_groups(){
    fetch("/api/group/", {
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
                state = {
                    groups: [...state.groups, {
                        id: group.id,
                        status: group.status,
                        note: group.note
                    }]
                }
            });
            updateState(state)
            
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
