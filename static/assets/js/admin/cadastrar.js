// Mask Functions
$(document).ready(function($){
  $('#rg').mask('00.000.000-0');
  $('#cep').mask('00000-000');
  $('#tel_residencial').mask('(00) 0000-0000');
  $('#tel_cel').mask('(00) 00000-0000');
  $('#tel_cel2').mask('(00) 00000-0000');
  $('#cpf').mask('000.000.000-00');
  $('#cnpj').mask('00.000.000/0000-00');
  $('#datepicker').mask('00/00/0000');
  $('#datepicker1').mask('00/00/0000');
  $('#datepicker2').mask('00/00/0000');
  })


//CEP
function limpa_formulário_cep() {
        //Limpa valores do formulário de cep.
        document.getElementById('cep').value=("");
        document.getElementById('rua').value=("");
        document.getElementById('bairro').value=("");
        document.getElementById('cidade').value=("");
        document.getElementById('uf').value=("");
}
function meu_callback(conteudo) {
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById('rua').value=(conteudo.logradouro);
        document.getElementById('bairro').value=(conteudo.bairro);
        document.getElementById('cidade').value=(conteudo.localidade);
        document.getElementById('uf').value=(conteudo.uf);
    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulário_cep();
        Swal.fire({
                      title: 'Erro !',
                      text: 'CEP não encontrado.',
                      icon: 'error',
                      confirmButtonText: 'Ok'
                    })
        //alert("CEP não encontrado.");
    }
}

function pesquisacep(valor) {

    //Nova variável "cep" somente com dígitos.
    var cep = valor.replace(/\D/g, '');

    //Verifica se campo cep possui valor informado.
    if (cep != "") {

        //Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if(validacep.test(cep)) {

            document.getElementById('cep').value = cep.substring(0,5)
            +"-"
            +cep.substring(5);

            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById('rua').value="...";
            document.getElementById('bairro').value="...";
            document.getElementById('cidade').value="...";
            document.getElementById('uf').value="...";

            //Cria um elemento javascript.
            var script = document.createElement('script');

            //Sincroniza com o callback.
            script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);

        } //end if.
        else {
            //cep é inválido.
            limpa_formulário_cep();
            Swal.fire({
                title: 'Erro !',
                    text: 'Formato de CEP inválido.',
                    icon: 'error',
                    confirmButtonText: 'Ok'
                        });
        }
    } //end if.
    else {
        //cep sem valor, limpa formulário.
        limpa_formulário_cep();
    }
};

//PRESTADOR DE SERVIÇOS CHECK_BUTTON
function form_Check() {
    if(document.form_consulta.checkbox.checked == true ){
    document.getElementById("dadoscomerciais").style.display = "grid";
    document.getElementById("dadoscomerciais").style.visibility = "visible";
    document.getElementById("dadoscomerciais").style.opacity = "1";
    document.getElementById("cnpj").required = true;
  }
    else if(document.form_consulta.checkbox.checked == false){
    document.getElementById("dadoscomerciais").style.visibility = "hidden";
    document.getElementById("dadoscomerciais").style.display = "None";
    document.getElementById("dadoscomerciais").style.opacity = "0";
    }
}

$('#datepicker').datepicker({
  locale: 'pt-br',
});
$('#datepicker1').datepicker({
  locale: 'pt-br',
});
$('#datepicker2').datepicker({
  locale: 'pt-br',
});


// VALIDAR CNPJ
function _cnpj(cnpj) {
	cnpj = cnpj.replace(/[^\d]+/g, '')

	// Valida a quantidade de caracteres
	if (cnpj.length !== 14)
		return false

	// Elimina inválidos com todos os caracteres iguais
	if (/^(\d)\1+$/.test(cnpj))
		return false

	// Cáculo de validação
	let t = cnpj.length - 2,
		d = cnpj.substring(t),
		d1 = parseInt(d.charAt(0)),
		d2 = parseInt(d.charAt(1)),
		calc = x => {
			let n = cnpj.substring(0, x),
				y = x - 7,
				s = 0,
				r = 0

				for (let i = x; i >= 1; i--) {
					s += n.charAt(x - i) * y--;
					if (y < 2)
						y = 9
				}

				r = 11 - s % 11
				return r > 9 ? 0 : r
		}

	return calc(t) === d1 && calc(t + 1) === d2
}

function ValidarCNPJ(el){
  if( !_cnpj(el.value) ){

    Swal.fire({
                title: 'Erro !',
                text: 'CNPJ inválido.',
                icon: 'error',
                confirmButtonText: 'Ok'
                });

    // apaga o valor
    el.value = "";
  }
}





//CPF VALIDAR_CPF
function _cpf(cpf) {
    cpf = cpf.replace(/[^\d]+/g, '');
    if (cpf == '') return false;
    if (cpf.length != 11 ||
        cpf == "00000000000" ||
        cpf == "11111111111" ||
        cpf == "22222222222" ||
        cpf == "33333333333" ||
        cpf == "44444444444" ||
        cpf == "55555555555" ||
        cpf == "66666666666" ||
        cpf == "77777777777" ||
        cpf == "88888888888" ||
        cpf == "99999999999")
        return false;
    add = 0;
    for (i = 0; i < 9; i++)
        add += parseInt(cpf.charAt(i)) * (10 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(9)))
        return false;
    add = 0;
    for (i = 0; i < 10; i++)
        add += parseInt(cpf.charAt(i)) * (11 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(10)))
        return false;
    return true;
}

function ValidarCPF(el){
    if( !_cpf(el.value) ){
        Swal.fire({
                title: 'Erro !',
                text: 'CPF inválido',
                icon: 'error',
                confirmButtonText: 'Ok'
                });
    // apaga o valor
    el.value = "";
    }
//    if (cpfs.includes(el.value)) {
//       Swal.fire({
//                title: 'Erro !',
//                text: 'CPF já cadastrado no sistema',
//                icon: 'info',
//                confirmButtonText: 'Ok'
//                });
//       el.value = "";
//    }
}



//Validar foto do usuário recebida
var file = document.getElementById('foto_usuario');

file.onchange = function(e) {
  var ext = this.value.match(/\.([^\.]+)$/)[1];
  switch (ext) {
    case 'jpg':
    case 'bmp':
    case 'png':
      break;
    default:
      Swal.fire({
                      title: 'Arquivo de imagem não suportado!',
                      text: 'Os arquivos suportado são jpg, bmp e png até 1mb.',
                      icon: 'error',
                      confirmButtonText: 'Ok'
                    });
      this.value = '';
  }
};


//Validar CPF, se o mesmo já existir no banco de dados.
$(function() {
    $("#cpf").on('blur', function() {
        $.ajax({
                url: $SCRIPT_ROOT+'/cpf_verify',
                type: 'GET',
                data: {cpf: $("#cpf").val()},
                dataType: 'html',
                contentType: 'text/html',
                success: function(){},
                error: function(){
                 Swal.fire(
                          '',
                          'CPF já cadastrado no sistema.. verifique novamente.',
                          'error'
                          )
                 cpf.value = ''}
                })
        })
    })


//Validar apelido, se o mesmo já existir no banco de dados.
$(function() {
    $("#apelido").on('blur', function() {
        $.ajax({
                url: $SCRIPT_ROOT+'/apelido_verify',
                type: 'GET',
                data: {apelido: $("#apelido").val()},
                dataType: 'html',
                contentType: 'text/html',
                success: function(){},
                error: function(){
                 Swal.fire(
                          '',
                          'Apelido já cadastrado no sistema.. verifique novamente.',
                          'error'
                          )
                 apelido.value = ''}
                })
        })
    })
