import React, { Component } from 'react'
import ManualSubmitter from './ManualSubmitter';
import Toggle from 'react-bootstrap-toggle';
import { language } from '../utils/language';

export default class Submitter extends Component {
    constructor(props) {
        super(props)
        this.state = {
            automated_on: true
        }
        this.change_submitter = this.change_submitter.bind(this)
    }

    change_submitter = () => {
        const { automated_on } = this.state
        this.setState({
            automated_on: !automated_on
        });

    }
    render() {
        const { selected_language } = this.props;
        const s_lang = language[selected_language];

        const { automated_on } = this.state;

        return (
            <>
                <div className="row d-flex justify-content-center">
                    <div className="col-md-12 pb-40 header-text text-center">
                        <h1 className="pb-10">{s_lang.t_cmm}</h1>
                        <p>
                            {s_lang.t_here}{(automated_on ? s_lang.t_on : s_lang.t_off)}
                        </p>
                        <Toggle on={s_lang.t_turn_it_off}
                            off={s_lang.t_turn_it_on}
                            size="xs"
                            offstyle="danger"
                            active={automated_on}
                            onClick={this.change_submitter} />
                    </div>
                </div>
                <div className="row">


                    <div className="col-lg-3 home-about-left no-padding">
                        <img className="img-fluid mx-auto" src="img/bot-ready.png" alt="" />
                    </div>
                    <div className="col-lg-6 col-md-6 blog-right">
                        {automated_on ? null : <ManualSubmitter manual_s_lang={selected_language} />}

                        <div className="form-group green-border-focus">
                            <label htmlFor="exampleFormControlTextarea5">{s_lang.t_each_line_hyp}</label>
                            <textarea placeholder={s_lang.t_input_conc} className="form-control" id="exampleFormControlTextarea5" rows="2"></textarea>
                        </div>
                        <div className="form-group green-border-focus">
                            <label htmlFor="exampleFormControlTextarea5">{s_lang.t_each_line_conc}</label>
                            <textarea placeholder="Each Conclusion should be in a separate line." className="form-control" id="exampleFormControlTextarea5" rows="2"></textarea>
                        </div>
                        <div className="form-group green-border-focus text-right">
                            <button className="btn btn-default" style={{ borderRadius: "50px" }}>
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
