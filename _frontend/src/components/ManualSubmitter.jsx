import React, { Component } from 'react'
import { language } from '../utils/language';

export default class ManualSubmitter extends Component {
    constructor(props) {
        super(props);
        this.doShit = this.doShit.bind(this)
    }
    doShit() {
        const file = this.fileUpload.files[0];
        console.log(file);
    }

    render() {
        const { manual_s_lang } = this.props;
        const manual_selected_language = language[manual_s_lang];
        // console.log(manual_s_lang);

        return (
            <>
                <div className="form-group purple-border">
                    <label htmlFor="input_full_text">{manual_selected_language.t_manual}</label>
                    <textarea className="form-control" id="input_full_text" rows="5"></textarea>
                </div>
                <div className="form-group purple-border">
                    <label htmlFor="input_full_text">{manual_selected_language.t_or}<br /></label>
                    <input className="form-control"
                        type='file' label='Upload'
                        //   buttonAfter={uploadFileButton} 
                        ref={(ref) => this.fileUpload = ref}
                    />
                    <button onClick={this.doShit}>ez</button>
                </div>
            </>
        )
    }
}
