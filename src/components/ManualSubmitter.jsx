import React, { Component } from 'react'
import { language } from '../utils/language';

export default class ManualSubmitter extends Component {
    render() {
        const { manual_s_lang } = this.props;
        const manual_selected_language=language[manual_s_lang];
        console.log(manual_s_lang);
        
        return (
            <>
                <div className="form-group purple-border">
                    <label htmlFor="input_full_text">{manual_selected_language.t_manual}</label>
                    <textarea className="form-control" id="input_full_text" rows="5"></textarea>
                </div>
                <div className="form-group purple-border">
                    <label htmlFor="input_full_text">{manual_selected_language.t_or}<br /></label>
                    <input className="form-control" type="file" />
                </div>
            </>
        )
    }
}
