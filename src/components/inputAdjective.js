import React from "react";

class InputAdjective extends React.Component {
    constructor() {
        super();
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event, adjIndex) {
        const newAdj = event.target.value;
        
        this.props.updateAdj(newAdj, adjIndex, this.props.dayDate);
    }

    render() {
        const adjValue = this.props.value;
        const dayDate = this.props.dayDate;

        if (adjValue) {
            return (
                <input
                    className="adjInput"
                    type="text"
                    name={this.props.name}
                    value={adjValue}
                    onChange={e => {
                        this.handleChange(e, this.props.name, dayDate);
                    }}
                />
            );
        } else {
            return (
                <input
                    className="adjInput"
                    type="text"
                    name={this.props.name}
                    placeholder="A Daily Adjective"
                    onChange={e => {
                        this.handleChange(e, this.props.name, dayDate);
                    }}
                />
            );
        }
    }
}

export default InputAdjective;
