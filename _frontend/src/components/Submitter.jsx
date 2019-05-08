import React, { Component } from 'react'
// import ManualSubmitter from './ManualSubmitter';
import Toggle from 'react-bootstrap-toggle';
import { language } from '../utils/language';
import axios from "axios";
export default class Submitter extends Component {
    constructor(props) {
        super(props)
        this.state = {
            manual_conclusion_base: "",
            manual_fact_base: "",
            manual_rules_base: "",
            mode_auto_activated: false,
            uploaded_file: null

        }
        this.change_submitter = this.change_submitter.bind(this)
        this.update_file_object = this.update_file_object.bind(this)
        this.handleChange = this.handleChange.bind(this)
        this.let_it_shine____baby = this.let_it_shine____baby.bind(this)
    }
    let_it_shine____baby() {
        let data = new FormData();
        data.append('manual_conclusion_base', this.state.manual_conclusion_base);
        data.append('manual_fact_base', this.state.manual_fact_base);
        data.append('manual_rules_base', this.state.manual_rules_base);
        data.append('mode_auto_activated', this.state.mode_auto_activated);
        data.append('uploaded_file', this.state.uploaded_file);
        // for (var p of data) {
        //     console.log(p);
        // }
        axios({
            method: 'post',
            url: 'http://127.0.0.1:5000/uploader',
            data: data,
            config: { headers: { 'Content-Type': 'multipart/form-data' } }
        }).then((response) => {
            //handle success
            console.log(response.data);
        }).catch((response) => {
            //handle error
            console.log(response);
        });

    }

    handleChange(event) {
        const { name, value } = event.target;
        this.setState({ [name]: value });
    }

    update_file_object() {
        this.setState({ uploaded_file: this.fileUpload.files[0] })
    }

    // componentDidUpdate(prev)

    change_submitter = () => {
        const { mode_auto_activated } = this.state
        this.setState({
            mode_auto_activated: !mode_auto_activated
        });
    }

    render() {
        const { selected_language } = this.props;
        const s_lang = language[selected_language];

        const { mode_auto_activated } = this.state;

        return (
            <>
                <div className="row d-flex justify-content-center">
                    <div className="col-md-12 pb-40 header-text text-center">
                        <h1 className="pb-10">{s_lang.t_cmm}</h1>
                        <p>
                            {s_lang.t_here}{(mode_auto_activated ? s_lang.t_on : s_lang.t_off)}
                        </p>
                        <Toggle on={s_lang.t_turn_it_off}
                            off={s_lang.t_turn_it_on}
                            size="xs"
                            offstyle="danger"
                            active={mode_auto_activated}
                            onClick={this.change_submitter} />
                    </div>
                </div>
                <div className="row">


                    <div className="col-lg-3 home-about-left no-padding">
                        <img className="img-fluid mx-auto" src="img/bot-ready.png" alt="" />
                    </div>
                    <div className="col-lg-6 col-md-6 blog-right">
                        {mode_auto_activated ? null :
                            <>
                                <div className="form-group purple-border">
                                    <label htmlFor="input_full_text">{s_lang.t_manual}</label>
                                    <textarea name="manual_rules_base" onChange={this.handleChange} className="form-control" id="input_full_text" rows="5"></textarea>
                                </div>
                                <div className="form-group purple-border">
                                    <label htmlFor="input_full_text">{s_lang.t_or}<br /></label>
                                    <input className="form-control"
                                        type='file' label='Upload'
                                        onChange={this.update_file_object}
                                        // name="manual_data_file" onChange={this.handleChange}
                                        //   buttonAfter={uploadFileButton} 
                                        ref={(ref) => this.fileUpload = ref}
                                    />
                                </div>
                                {/* {this.state.server_upload_url == "" ? null :
                                    <iframe src={this.state.server_upload_url} id="ez" />} */}
                            </>
                            // <ManualSubmitter manual_s_lang={selected_language} />
                        }

                        <div className="form-group green-border-focus">
                            <label htmlFor="exampleFormControlTextarea5">{s_lang.t_each_line_hyp}</label>
                            <textarea name="manual_fact_base" onChange={this.handleChange}
                                placeholder={s_lang.t_input_conc} className="form-control" id="exampleFormControlTextarea5" rows="2"></textarea>
                        </div>
                        <div className="form-group green-border-focus">
                            <label htmlFor="exampleFormControlTextarea5">{s_lang.t_each_line_conc}</label>
                            <textarea
                                name="manual_conclusion_base" onChange={this.handleChange}
                                placeholder="Each Conclusion should be in a separate line." className="form-control" id="exampleFormControlTextarea5" rows="2"></textarea>
                        </div>
                        <div className="form-group green-border-focus text-right">
                            <button className="btn btn-default" style={{ borderRadius: "50px" }} onClick={this.let_it_shine____baby}>
                                <span className="lnr lnr-magic-wand"></span>&nbsp;{s_lang.t_execute}
                            </button>
                        </div>

                    </div>
                    <div className="col-lg-3 ">
                    </div>

                </div>
            </>
        )
    }
}
