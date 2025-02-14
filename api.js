const baseUrl = 'http://127.0.0.1:5000'
async function fetchTodos() {
    try {
        const response =await fetch(`${baseUrl}/get_todo`)
        console.log(response)
        const todos = await response.json()
        return todos;
    } catch (error) {
                console.log(error)
    }
}
async function createtodo(title) {
    try {
        fetch(`${baseUrl}/add_todo`, 
            {method:'POST',
            headers:{
                'content-Type':'application/json'
            },
            body:JSON.stringify({title}),
            })
            return true
            }

        
    catch  (error){  
    }
}
