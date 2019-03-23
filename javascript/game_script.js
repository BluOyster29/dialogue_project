var name = [];

    function add_letter(letter){
      name.push(letter);
      return name
      
    }

    function read_name(){
      name = name.join('');
      return name.toString()

  }

  function reset_name(name){
    name = [];
    return name
  }