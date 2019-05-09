import React, { Component } from "react";
import "./App.css";
import Submitter from "./components/Submitter";
import { language } from "./utils/language";
import ChatBot from "react-simple-chatbot"; 

const  steps=[
      {
        id: '0',
        message: 'Hi! I am CMMB you need some help?',
        trigger:'1'
      },
      {
        id: '1',
        options: [
          { value: 1, label: 'Yes!', trigger: '2' },
        ],
      },
      
      {
        id: '2',
        message: `Excellent! I am CMMB.
        I can "change your mind" by finding the logic between rules, hypothesis and the goal you serve.
        So what do you want me to do?`,
        trigger:"2.1"
      },
      {id:"2.1",
      options: [
        { value: 1, label: 'I want to try!', trigger: '3' },
      ],},
      {
        id: '3',
        message: 'No Problem. Scroll to the bottom of this page to find out more!',
        end: true,
      },
    ]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selected_language: "en"
    };
    this.swap_lang = this.swap_lang.bind(this);
  }
  swap_lang() {
    this.setState({
      selected_language: this.state.selected_language === "fr" ? "en" : "fr"
    });
  }
  render() {
    const { selected_language } = this.state;
    const current_user_language = language[selected_language];
    let other_lang = this.state.selected_language === "fr" ? "en" : "fr";
    return (
      <>
        <header id="header">
          <div className="container main-menu ">
              <ChatBot steps={steps} floating={true} />
            <div className="row align-items-center justify-content-between d-flex">
              <div id="logo">
                <a href="index.html" className="text-light">
                  <img
                    src="img/bot-hi.png"
                    alt="bad"
                    title=""
                    style={{ maxWidth: "50px" }}
                  />
                  {"CMM-B"}
                </a>
              </div>
              <nav id="nav-menu-container">
                <ul className="nav-menu">
                  <li className="menu-active">
                    <a href="#home">{current_user_language.t_home} </a>
                  </li>
                  <li>
                    <a href="#introduction">
                      {current_user_language.t_introduction}
                    </a>
                  </li>
                  <li>
                    <a href="#abilities">{current_user_language.t_abilities}</a>
                  </li>
                  <li>
                    <a href="#features">{current_user_language.t_features}</a>
                  </li>
                  <li>
                    <a href="#playground">
                      {current_user_language.t_playground}
                    </a>
                  </li>
                  <li className="menu-has-children">
                    <div className="btn btn-link">
                      {current_user_language.main_display}
                    </div>
                    <ul className="nav-menu">
                      <li>
                        <button
                          onClick={this.swap_lang}
                          className="btn btn-link"
                        >
                          {language[other_lang].selector}
                        </button>
                      </li>
                    </ul>
                  </li>
                </ul>
              </nav>
              {/* <!-- #nav-menu-container --> */}
            </div>
          </div>
        </header>
        {/*
  <!-- #header --> */}

        {/* <!-- start banner Area --> */}
        <section className="banner-area" id="home">
          <div className="container">
            <div className="row fullscreen d-flex align-items-center justify-content-center">
              <div className="banner-content col-lg-6 col-md-6">
                <h1>{current_user_language.t_welcome}</h1>
                <p className="text-white text-uppercase">
                  {current_user_language.t_the_change}
                </p>
                <a
                  href="#introduction"
                  className="primary-btn header-btn text-uppercase"
                >
                  {current_user_language.t_find}
                </a>
              </div>
              <div className="banner-img col-lg-6 col-md-6">
                <img
                  className="vert-move img-fluid"
                  src="img/bot-hi.png"
                  alt="bad"
                />
              </div>
            </div>
          </div>
        </section>
        {/* <!-- End banner Area --> */}

        {/* <!-- Start home-about Area --> */}
        <section className="home-about-area" id="introduction">
          <div className="container-fluid">
            <div className="row align-items-center">
              <div className="col-lg-6 home-about-left no-padding">
                <img
                  className="mx-auto d-block img-fluid"
                  src="img/bot-init.png"
                  alt="bad"
                />
              </div>
              <div className="col-lg-6 home-about-right no-padding">
                <h1>{current_user_language.t_the_making}</h1>
                <h5>{current_user_language.t_it_spell}</h5>
                <p>{current_user_language.t_based_on_algo}</p>
                <a className="primary-btn text-uppercase" href="#abilities">
                  {current_user_language.t_know}
                </a>
              </div>
            </div>
          </div>
        </section>
        {/* <!-- End home-about Area --> */}

        {/* <!-- Start about-video Area --> */}
        <section id="abilities" className="about-video-area section-gap">
          <div className="container">
            <div className="row align-items-center">
              <div className="col-lg-6 about-video-left">
                <h6 className="text-uppercase">
                  {current_user_language.t_how}
                </h6>
                <h1>{current_user_language.t_it_more}</h1>
                <p>
                  <span>{current_user_language.t_it_much}</span>
                </p>
                <p>{current_user_language.t_based_on_input}</p>
                <a className="primary-btn" href="#playground">
                  {current_user_language.t_get}
                </a>
              </div>
              <div className="col-lg-6 home-about-left no-padding">
                <img
                  className="img-fluid mx-auto"
                  src="img/bot-search.svg"
                  alt="bad"
                />
              </div>
            </div>
          </div>
        </section>
        {/* <!-- End about-video Area --> */}

        {/* <!-- Start feature Area --> */}
        <section id="features" className="feature-area section-gap">
          <div className="container">
            <div className="row d-flex justify-content-center">
              <div className="col-md-12 pb-40 header-text text-center">
                <h1 className="pb-10 text-white">
                  {current_user_language.t_some}
                </h1>
                <p className="text-white">
                  {current_user_language.t_the_b_stands}
                  <i className="fa fa-heart-o" aria-hidden="true" />.
                </p>
              </div>
            </div>
            <div className="row">
              <div className="col-lg-4 col-md-6">
                <div className="single-feature">
                  <div className="title d-flex flex-row">
                    <span className="lnr lnr-sort-amount-asc" />
                    <h4>{current_user_language.t_optimised}</h4>
                  </div>
                  <p>{current_user_language.t_ithandles}</p>
                </div>
              </div>
              <div className="col-lg-4 col-md-6">
                <div className="single-feature">
                  <div className="title d-flex flex-row">
                    <span className="lnr lnr-users" />
                    <h4>{current_user_language.t_human}</h4>
                  </div>
                  <p>{current_user_language.t_inspired}</p>
                </div>
              </div>
              <div className="col-lg-4 col-md-6">
                <div className="single-feature">
                  <div className="title d-flex flex-row">
                    <span className="lnr lnr-spell-check" />
                    <h4>{current_user_language.t_bilingual}</h4>
                  </div>
                  <p>{current_user_language.t_starting}</p>
                </div>
              </div>
              <div className="col-lg-4 col-md-6">
                <div className="single-feature">
                  <div className="title d-flex flex-row">
                    <span className="lnr lnr-rocket" />
                    <h4>{current_user_language.t_laziness}</h4>
                  </div>
                  <p>{current_user_language.t_if}</p>
                </div>
              </div>
              <div className="col-lg-4 col-md-6">
                <div className="single-feature">
                  <div className="title d-flex flex-row">
                    <span className="lnr lnr-diamond" />
                    <h4>{current_user_language.t_highly}</h4>
                  </div>
                  <p>{current_user_language.t_swift}</p>
                </div>
              </div>
              <div className="col-lg-4 col-md-6">
                <div className="single-feature">
                  <div className="title d-flex flex-row">
                    <span className="lnr lnr-bubble" />
                    <h4>{current_user_language.t_positive}</h4>
                  </div>
                  <p>
                    {current_user_language.t_by_our}
                    <a href="#playground">{current_user_language.t_go_ahead}</a>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>
        {/* <!-- End feature Area --> */}

        {/* <!-- Start blog Area --> */}
        <section id="playground" className="blog-area section-gap">
          <div className="container">
            <Submitter selected_language={this.state.selected_language} />
          </div>
        </section>
        {/* <!-- End blog Area --> */}
        {/* <!-- Back to top button--> */}
        {/* <a href="#home" id="back-to-top" title="Back to top">&uarr;</a> */}
        {/* <!-- Back to top button--> */}

        {/* <!-- start footer Area --> */}
        <footer className="footer-area">
          <div className="container">
            <div className="row">
              <div className="col-lg-12  col-md-12">
                <div className="single-footer-widget newsletter">
                  <h6>{current_user_language.t_made}</h6>
                </div>
              </div>
            </div>

            <div className="row footer-bottom d-flex justify-content-between">
              <p className="col-lg-8 col-sm-12 footer-text m-0 text-white">
                {/* <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --> */}
                {current_user_language.t_copyright} &copy;
                <script>{new Date().getFullYear()}</script>{" "}
                {current_user_language.t_all}{" "}
                <i className="fa fa-heart-o" aria-hidden="true" />{" "}
                {current_user_language.t_by} {"P&R"}
                {/* <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --> */}
              </p>
              <div className="col-lg-4 col-sm-12 footer-social">
                <a href="#playground">
                  <i className="fa fa-facebook" />
                </a>
                <a href="#playground">
                  <i className="fa fa-twitter" />
                </a>
                <a href="#playground">
                  <i className="fa fa-dribbble" />
                </a>
                <a href="#playground">
                  <i className="fa fa-behance" />
                </a>
              </div>
            </div>
          </div>
        </footer>
        {/* <!-- End footer Area --> */}
      </>
    );
  }
}

export default App;
