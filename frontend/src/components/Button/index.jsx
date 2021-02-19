import React from 'react';


const Button = props => {
    return (
        <button onClick={props.onClick} type={"button"}
                className={`btn btn-${props.bg} font-weight-${props.weight}  font-size-${props.fontSize} ${props.className}`}>{props.children}
        </button>
    )
}


export default Button;