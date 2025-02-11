function addTodo() {
    const todoText = todoInput.value.trim();
    if (todoText === "") {
      return;
    }
    const li = document.createElement("li");
    li.innerHTML = `
      <input type="checkbox" onchange="toggleTodo(this)">
      <span>${todoText}</span>
      <button class="delete-btn" onclick="deleteTodo(this)">Delete</button>
      `;
    todoList.appendChild(li);
    todoInput.value = "";
    updateEmptyMessage();
  }
  function deleteTodo(button){
    button.parentElement.remove();
  }
  function editTodo(){
    let edit = prompt("Edit your task");
    if(edit!=null){
        document.getElementById("todoInput").value = edit;
    }
    
  }
