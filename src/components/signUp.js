import React from 'react';

class SignUp extends React.Component {
    
    constructor(){
        super();
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(e){
        e.preventDefault();
        const email1 = this.email1.value;
        const email2 = this.email2.value;
        const password1 = this.password1.value;
        const password2 = this.password2.value;
        document.getElementById('signUpForm').reset();
        console.log(email1,password1);
        this.props.onSignUp(email1, email2, password1, password2);
    }



    render(){
        return(

            <div> 
                <div id="intro">
                    <h1> Welcome to Daily; the emotion tracking calendar! </h1>
                    <h2> This calendar application helps you to track your daily emotional well-being. Just by typing in three adjectives and chosing an associated color! </h2> 
                </div>
                
                <form id="signUpForm"> 
                    <h3> SignUp for Daily: </h3>
                    <input type="text" ref={(input) =>{this.email1 = input; }} placeholder="email"/>
                    <br/>
                    <input type="text" ref={(input) =>{this.email2 = input; }} placeholder="retype your email"/>
                    <br/>
                    <input type="password" ref={(input) =>{this.password1 = input; }} placeholder="password"/>
                    <br/>
                    <input type="password" ref={(input) =>{this.password2 = input; }} placeholder="retype your password" />
                    <br/>
                    <input type="submit" value="SignUp" onClick={(e)=>{this.handleClick(e)}}/>  
                </form>
            </div>
        )
    }
}

export default SignUp;