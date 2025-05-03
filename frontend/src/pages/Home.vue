<template>
  <div class="background">
    <div class="bg-gradient"></div>
    <div class="bg-grid"></div>
    <div class="floating-orbs">
      <div class="orb"></div>
      <div class="orb"></div>
      <div class="orb"></div>
    </div>
    <div class="data-points">
      <div class="data-point"></div>
      <div class="data-point"></div>
      <div class="data-point"></div>
      <div class="data-point"></div>
      <div class="data-point"></div>
    </div>
  </div>

  <div class="container">
    <nav class="navbar">
      <a href="#" class="logo">
        <div class="logo-icon">
          <!-- <svg width="20" height="20" viewBox="0 0 24 24" fill="white">
            <path d="M12 2L2 7L12 12L22 7L12 2Z"></path>
            <path d="M2 17L12 22L22 17"></path>
            <path d="M2 12L12 17L22 12"></path>
          </svg> -->
          <img src="../../public/finly_whisper_weallth.png" alt="Finly Logo" width="30" height="30" viewBox="0 0 24 24"
            fill="white" style="filter: brightness(0) invert(1);" />

        </div>
        <img src="../../public/finly.png" alt="Finly Logo" width="100" height="30"
          style="filter: brightness(0) invert(1); margin-left: -10%;" />

      </a>

      <div class="nav-links">
        <a href="#" class="nav-link">About</a>
        <a href="#our-services" class="nav-link">Our Services</a>
        <a href="#highlights" class="nav-link">Highlights</a>
        <a href="#" class="nav-link">Pricing</a>
      </div>

      <div class="cta">
        <a href="https://two-korecent.frappe.cloud/app/dashboard-view/My%20Activity" class="login-btn">Log In</a>
      </div>
    </nav>

    <div class="hero">
      <div class="hero-content">
        <div class="hero-subtitle">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <path d="M12 6v6l4 2"></path>
          </svg>
          AI-Powered Expense Management
        </div>

        <h1 class="hero-title">Manage Your Expenses With Finly AI</h1>

        <p class="hero-description">
          Finly is an intelligent, AI-driven expense management solution that
          streamlines personal finance tracking and empowers you with real-time
          insights. Simply chat with our AI to track, categorize, and monitor
          your Expenses.
        </p>

        <div class="hero-buttons">
          <a href="https://two-korecent.frappe.cloud/primary-account/new" class="btn btn-primary">
            Get Started
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"></path>
              <path d="M12 5l7 7-7 7"></path>
            </svg>
          </a>
          <!-- <a href="#" class="btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <polygon points="10 8 16 12 10 16 10 8"></polygon>
            </svg>
            Watch Demo
          </a> -->
        </div>

        <div class="features-pill">
          <div class="feature">
            <svg class="feature-icon" viewBox="0 0 24 24" fill="currentColor">
              <path
                d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M12,10.5A1.5,1.5 0 0,1 13.5,12A1.5,1.5 0 0,1 12,13.5A1.5,1.5 0 0,1 10.5,12A1.5,1.5 0 0,1 12,10.5M7.5,10.5A1.5,1.5 0 0,1 9,12A1.5,1.5 0 0,1 7.5,13.5A1.5,1.5 0 0,1 6,12A1.5,1.5 0 0,1 7.5,10.5M16.5,10.5A1.5,1.5 0 0,1 18,12A1.5,1.5 0 0,1 16.5,13.5A1.5,1.5 0 0,1 15,12A1.5,1.5 0 0,1 16.5,10.5Z" />
            </svg>
            AI-Powered
          </div>
          <div class="feature">
            <svg class="feature-icon" viewBox="0 0 24 24" fill="currentColor">
              <path
                d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M12,10.5A1.5,1.5 0 0,1 13.5,12A1.5,1.5 0 0,1 12,13.5A1.5,1.5 0 0,1 10.5,12A1.5,1.5 0 0,1 12,10.5M7.5,10.5A1.5,1.5 0 0,1 9,12A1.5,1.5 0 0,1 7.5,13.5A1.5,1.5 0 0,1 6,12A1.5,1.5 0 0,1 7.5,10.5M16.5,10.5A1.5,1.5 0 0,1 18,12A1.5,1.5 0 0,1 16.5,13.5A1.5,1.5 0 0,1 15,12A1.5,1.5 0 0,1 16.5,10.5Z" />
            </svg>
            Voice Commands
          </div>
          <div class="feature">
            <svg class="feature-icon" viewBox="0 0 24 24" fill="currentColor">
              <path
                d="M12,2A10,10 0 0,1 22,12A10,10 0 0,1 12,22A10,10 0 0,1 2,12A10,10 0 0,1 12,2M12,4A8,8 0 0,0 4,12A8,8 0 0,0 12,20A8,8 0 0,0 20,12A8,8 0 0,0 12,4M12,10.5A1.5,1.5 0 0,1 13.5,12A1.5,1.5 0 0,1 12,13.5A1.5,1.5 0 0,1 10.5,12A1.5,1.5 0 0,1 12,10.5M7.5,10.5A1.5,1.5 0 0,1 9,12A1.5,1.5 0 0,1 7.5,13.5A1.5,1.5 0 0,1 6,12A1.5,1.5 0 0,1 7.5,10.5M16.5,10.5A1.5,1.5 0 0,1 18,12A1.5,1.5 0 0,1 16.5,13.5A1.5,1.5 0 0,1 15,12A1.5,1.5 0 0,1 16.5,10.5Z" />
            </svg>
            Real-time Insights
          </div>
        </div>
      </div>

      <div class="hero-visual">
        <div class="dashboard-wrapper">
          <div class="dashboard">
            <div class="dashboard-content">
              <div class="dashboard-header">
                <div class="dashboard-title">Financial Overview</div>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <circle cx="12" cy="12" r="1"></circle>
                  <circle cx="19" cy="12" r="1"></circle>
                  <circle cx="5" cy="12" r="1"></circle>
                </svg>
              </div>

              <div class="dashboard-body">
                <div class="stat-card">
                  <div class="stat-title">Monthly Budget</div>
                  <div class="stat-value">$3,500</div>
                </div>

                <div class="stat-card">
                  <div class="stat-title">Total Spent</div>
                  <div class="stat-value">$2,145</div>
                </div>

                <div class="expenses-chart">
                  <div class="chart-title">Weekly Expenses</div>
                  <div class="chart">
                    <div class="chart-bar"></div>
                    <div class="chart-bar"></div>
                    <div class="chart-bar"></div>
                    <div class="chart-bar"></div>
                    <div class="chart-bar"></div>
                    <div class="chart-bar"></div>
                    <div class="chart-bar"></div>
                  </div>
                </div>

                <div class="transactions">
                  <div class="transaction-item">
                    <div class="transaction-left">
                      <div class="transaction-icon">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"
                          stroke-linecap="round" stroke-linejoin="round">
                          <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                          <circle cx="12" cy="10" r="3"></circle>
                        </svg>
                      </div>
                      <div class="transaction-details">
                        <div class="transaction-name">Starbucks</div>
                        <div class="transaction-date">Today, 9:45 AM</div>
                      </div>
                    </div>
                    <div class="transaction-amount">-$8.50</div>
                  </div>

                  <div class="transaction-item">
                    <div class="transaction-left">
                      <div class="transaction-icon">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"
                          stroke-linecap="round" stroke-linejoin="round">
                          <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                          <line x1="16" y1="2" x2="16" y2="6"></line>
                          <line x1="8" y1="2" x2="8" y2="6"></line>
                          <line x1="3" y1="10" x2="21" y2="10"></line>
                        </svg>
                      </div>
                      <div class="transaction-details">
                        <div class="transaction-name">Netflix Subscription</div>
                        <div class="transaction-date">Yesterday, 11:20 PM</div>
                      </div>
                    </div>
                    <div class="transaction-amount">-$15.99</div>
                  </div>

                  <div class="transaction-item">
                    <div class="transaction-left">
                      <div class="transaction-icon">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"
                          stroke-linecap="round" stroke-linejoin="round">
                          <path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z">
                          </path>
                          <line x1="7" y1="7" x2="7.01" y2="7"></line>
                        </svg>
                      </div>
                      <div class="transaction-details">
                        <div class="transaction-name">Grocery Shopping</div>
                        <div class="transaction-date">Apr 24, 6:30 PM</div>
                      </div>
                    </div>
                    <div class="transaction-amount">-$78.35</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Services Section -->
  <section class="services-section" id="our-services">
    <div class="container">
      <div class="section-header">
        <div class="section-label">Our Services</div>
        <h2 class="section-title">
          Powerful Features to Revolutionize Your Financial Management
        </h2>
        <p class="section-description">
          Our AI-powered platform provides intuitive tools designed to simplify
          and enhance your financial management like never before.
        </p>
      </div>

      <div class="services-grid">
        <div class="service-card">
          <div class="service-icon-wrapper">
            <div class="service-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
              </svg>
            </div>
          </div>
          <h3 class="service-title">Smart Expense Tracking</h3>
          <p class="service-description">
            Take control of your financial life by categorizing and tracking all
            your expenses in real-time. Finly allows you to create custom
            categories based on your unique needs and automatically logs your
            spending, ensuring you always stay on top of your budget.
          </p>
          <a href="#" class="service-link">Learn More
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"></path>
              <path d="M12 5l7 7-7 7"></path>
            </svg>
          </a>
        </div>

        <div class="service-card">
          <div class="service-icon-wrapper">
            <div class="service-icon">
              <!-- Globe icon for multilingual support -->
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path d="M12 2a15.3 15.3 0 0 1 0 20"></path>
                <path d="M12 2a15.3 15.3 0 0 0 0 20"></path>
              </svg>
            </div>
          </div>
          <h3 class="service-title">Multilingual Voice Support</h3>
          <p class="service-description">
            Effortlessly track your expenses in any language. Finly’s AI-powered
            multilingual voice recognition lets you log, categorize, and manage
            your finances with ease—just speak, and Finly understands.
          </p>
          <a href="#" class="service-link">
            Learn More
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"></path>s
              <path d="M12 5l7 7-7 7"></path>
            </svg>
          </a>
        </div>

        <div class="service-card">
          <div class="service-icon-wrapper">
            <div class="service-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round">
                <path d="M21.21 15.89A10 10 0 1 1 8 2.83"></path>
                <path d="M22 12A10 10 0 0 0 12 2v10z"></path>
              </svg>
            </div>
          </div>
          <h3 class="service-title">Event Scheduling & Budget Management</h3>
          <p class="service-description">
            Receive weekly spending summaries, set monthly budgets for specific
            categories, and get instant alerts when your budget is close to
            exceeding or if your balance is running low. Finly ensures that
            you're always informed and prepared.
          </p>
          <a href="#" class="service-link">Learn More
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"></path>
              <path d="M12 5l7 7-7 7"></path>
            </svg>
          </a>
        </div>

        <div class="service-card">
          <div class="service-icon-wrapper">
            <div class="service-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round">
                <line x1="12" y1="20" x2="12" y2="10"></line>
                <line x1="18" y1="20" x2="18" y2="4"></line>
                <line x1="6" y1="20" x2="6" y2="16"></line>
              </svg>
            </div>
          </div>
          <h3 class="service-title">Advanced Financial Insights</h3>
          <p class="service-description">
            Unlock deep insights into your financial habits with Finly’s
            intelligent AI analytics. Understand your spending patterns,
            identify opportunities for savings, and receive personalized
            recommendations tailored to your financial goals.
          </p>
          <a href="#" class="service-link">Learn More
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"></path>
              <path d="M12 5l7 7-7 7"></path>
            </svg>
          </a>
        </div>
      </div>

      <div class="service-highlight" id="highlights">
        <div class="highlight-content">
          <h3 class="highlight-title">
            Ready to Take Control of Your Finances?
          </h3>
          <p class="highlight-description">
            Unlock smarter, effortless expense management with Finly’s
            AI-powered insights.
          </p>
          <a href="https://two-korecent.frappe.cloud/primary-account/new" class="btn btn-primary">
            Start Your Free Trial
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"></path>
              <path d="M12 5l7 7-7 7"></path>
            </svg>
          </a>
        </div>
        <div class="highlight-visual">
          <div class="phone-mockup">
            <div class="phone-screen">
              <div class="chat-interface">
                <div class="chat-header">
                  <div class="chat-avatar"></div>
                  <div class="chat-title">Finly</div>
                </div>
                <div class="chat-messages">
                  <!-- Audio message from user -->
                  <div class="chat-message user">
                    <div class="audio-message">
                      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path>
                        <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
                        <line x1="12" y1="19" x2="12" y2="22"></line>
                      </svg>
                      <div class="audio-waveform">
                        <span></span><span></span><span></span><span></span><span></span>
                      </div>
                      <span class="audio-duration">0:08</span>
                    </div>
                  </div>

                  <!-- Bot responses for audio processing -->
                  <div class="chat-message bot">
                    <div class="typing-indicator">
                      <span></span><span></span><span></span>
                    </div>
                    <div class="message-text" style="display: none;">Processing...</div>
                  </div>

                  <div class="chat-message bot">
                    <div class="typing-indicator">
                      <span></span><span></span><span></span>
                    </div>
                    <div class="message-text" style="display: none;">
                      Hold tight! We're transcribing your audio.
                    </div>
                  </div>

                  <div class="chat-message bot">
                    <div class="typing-indicator">
                      <span></span><span></span><span></span>
                    </div>
                    <div class="message-text" style="display: none;">Almost Done!</div>
                  </div>

                  <div class="chat-message bot">
                    <div class="typing-indicator">
                      <span></span><span></span><span></span>
                    </div>
                    <div class="message-text" style="display: none;">
                      <strong>Transcription Complete!</strong><br />
                      "I spent two hundred on Uber."<br /><br />
                      <strong>Expense Summary</strong><br />
                      <span class="expense-item">Amount: ₹ 200.00</span><br />
                      <span class="expense-item">Category: Transport</span><br />
                      <span class="expense-item">Merchant: Uber</span><br /><br />
                      Your expense has been successfully recorded.<br />
                      <em>Stay on top of your finances with effortless tracking!</em>
                    </div>
                  </div>
                </div>

                <div class="chat-input">
                  <input type="text" placeholder="Send a message..." />
                  <button class="send-button">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                      stroke-linecap="round" stroke-linejoin="round">
                      <line x1="22" y1="2" x2="11" y2="13"></line>
                      <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                    </svg>
                  </button>
                  <button class="voice-button">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                      stroke-linecap="round" stroke-linejoin="round">
                      <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3z"></path>
                      <path d="M19 10v2a7 7 0 0 1-14 0v-2"></path>
                      <line x1="12" y1="19" x2="12" y2="22"></line>
                    </svg>
                  </button>
                </div>
              </div>
            </div>
            <div class="phone-notch"></div>
            <div class="phone-button"></div>
            <div class="glow-effect"></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Testimonials Section -->
  <section class="testimonials-section" style="display: none">
    <div class="container">
      <div class="section-header">
        <div class="section-label">Testimonials</div>
        <h2 class="section-title">What Our Users Say</h2>
      </div>

      <div class="testimonials-slider">
        <div class="testimonial-track">
          <div class="testimonial-card">
            <div class="testimonial-content">
              <div class="quote-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 21c3.73-2.43 5.57-5.2 5.57-10V3h6v8c0 4.8 1.84 7.57 5.57 10"></path>
                </svg>
              </div>
              <p class="testimonial-text">
                Finly has completely transformed how I manage my finances. The
                AI assistant feels like having a personal financial advisor
                available 24/7.
              </p>
              <div class="testimonial-author">
                <div class="author-avatar"></div>
                <div class="author-info">
                  <div class="author-name">Sarah Johnson</div>
                  <div class="author-title">Freelance Designer</div>
                </div>
              </div>
            </div>
          </div>

          <div class="testimonial-card">
            <div class="testimonial-content">
              <div class="quote-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 21c3.73-2.43 5.57-5.2 5.57-10V3h6v8c0 4.8 1.84 7.57 5.57 10"></path>
                </svg>
              </div>
              <p class="testimonial-text">
                The insights and recommendations are spot-on. I've saved over
                $500 monthly since I started using Finly to manage my budget.
              </p>
              <div class="testimonial-author">
                <div class="author-avatar"></div>
                <div class="author-info">
                  <div class="author-name">Michael Chen</div>
                  <div class="author-title">Software Engineer</div>
                </div>
              </div>
            </div>
          </div>

          <div class="testimonial-card">
            <div class="testimonial-content">
              <div class="quote-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                  stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 21c3.73-2.43 5.57-5.2 5.57-10V3h6v8c0 4.8 1.84 7.57 5.57 10"></path>
                </svg>
              </div>
              <p class="testimonial-text">
                As someone who always struggled with financial planning, Finly
                has been a game changer. The interface is intuitive and the AI
                actually understands my goals.
              </p>
              <div class="testimonial-author">
                <div class="author-avatar"></div>
                <div class="author-info">
                  <div class="author-name">Emma Rodriguez</div>
                  <div class="author-title">Marketing Manager</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="slider-controls">
          <button class="slider-arrow prev">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M19 12H5"></path>
              <path d="M12 19l-7-7 7-7"></path>
            </svg>
          </button>
          <div class="slider-dots">
            <span class="dot active"></span>
            <span class="dot"></span>
            <span class="dot"></span>
          </div>
          <button class="slider-arrow next">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M5 12h14"></path>
              <path d="M12 5l7 7-7 7"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer" ref="footer">
    <div class="footer-gradient"></div>
    <div class="particles-container" ref="particles"></div>

    <div class="container">
      <div class="footer-top">
        <div class="footer-brand" ref="footerBrand">
          <a href="#" class="footer-logo">
            <div class="logo-icon">
              <img src="../../public/finly_whisper_weallth.png" alt="Finly Logo" width="30" height="30"
                style="filter: brightness(0) invert(1);" />
            </div>
            <img src="../../public/finly.png" alt="Finly Logo" width="100" height="30"
              style="filter: brightness(0) invert(1); margin-left: -5%;" />
          </a>
          <p class="footer-tagline" ref="tagline">
            AI-powered expense management for smarter financial decisions.
          </p>
          <div class="social-links" ref="socialLinks">
            <a href="#" class="social-link" v-for="(icon, index) in socialIcons" :key="index"
              @mouseover="animateSocialIcon" @mouseout="resetSocialIcon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round" v-html="icon"></svg>
            </a>
          </div>
        </div>

        <div class="footer-subscribe" ref="subscribeBox">
          <h4 class="subscribe-title">Stay Connected</h4>
          <p class="subscribe-text">
            Join our community to receive the latest updates and feature announcements directly to your inbox.
          </p>
          <form class="subscribe-form" @submit.prevent="handleSubscribe">
            <input type="email" placeholder="Your email address" required ref="emailInput" />
            <button type="submit" class="btn btn-primary subscribe-btn" ref="subscribeBtn">
              <span>Subscribe</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                stroke-linecap="round" stroke-linejoin="round">
                <path d="M5 12h14"></path>
                <path d="M12 5l7 7-7 7"></path>
              </svg>
            </button>
          </form>
        </div>
      </div>

      <div class="footer-bottom" ref="footerBottom">
        <div class="copyright">&copy; {{ currentYear }} Finly, All rights reserved.</div>
        <div class="footer-badges">
          <div class="badge security-badge" ref="securityBadge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
            <span class="badge-text">256-bit Encryption</span>
          </div>
          <div class="badge terms-badge" ref="termsBadge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" stroke-linejoin="round">
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
            </svg>
            <a href="#" class="terms-link">Terms & Conditions</a>
            <span class="divider">|</span>
            <a href="#" class="privacy-link">Privacy Policy</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  mounted() {
    // Once Vue component is mounted, initialize animations
    this.initChatAnimation();
    this.initScrollAnimations();
  },
  methods: {
    initChatAnimation() {
      // Chat animation functionality
      const chatMessages = document.querySelectorAll('.chat-message.bot');
      chatMessages.forEach((message, index) => {
        const typingIndicator = message.querySelector('.typing-indicator');
        const messageText = message.querySelector('.message-text');

        // Show typing indicator and then show message
        setTimeout(() => {
          if (typingIndicator) {
            typingIndicator.style.display = 'flex';
          }

          setTimeout(() => {
            if (typingIndicator) {
              typingIndicator.style.display = 'none';
            }

            if (messageText) {
              messageText.style.display = 'block';
              messageText.style.opacity = '0';

              // Fade in the message
              let opacity = 0;
              const fadeIn = setInterval(() => {
                opacity += 0.1;
                messageText.style.opacity = opacity;
                if (opacity >= 1) {
                  clearInterval(fadeIn);
                }
              }, 40);
            }
          }, 1500);
        }, index * 3000);
      });
    },
    initScrollAnimations() {
      // Animate service cards on scroll using Intersection Observer
      const serviceCards = document.querySelectorAll('.service-card');

      const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px'
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('fade-in-up');
            observer.unobserve(entry.target);
          }
        });
      }, observerOptions);

      serviceCards.forEach(card => {
        observer.observe(card);
      });

      // Section visibility animation
      const servicesSection = document.querySelector('.services-section');
      const footer = document.querySelector('.footer');

      const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('section-visible');
            sectionObserver.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.1
      });

      if (servicesSection) {
        sectionObserver.observe(servicesSection);
      }

      if (footer) {
        sectionObserver.observe(footer);
      }
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Outfit', sans-serif;
}

:root {
  --primary: #3a86ff;
  --primary-light: #61a0ff;
  --secondary: #8338ec;
  --accent: #ff006e;
  --light: #f8f9fa;
  --dark: #090e1a;
  --gradient: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
  --glass: rgba(255, 255, 255, 0.1);
  --shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}

body {
  background-color: var(--dark);
  color: var(--light);
  /* height: 100vh; */
  overflow-y: auto;
  position: relative;
}

.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  overflow: hidden;
}

.bg-gradient {
  position: absolute;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 70% 30%,
      rgba(131, 56, 236, 0.15) 0%,
      rgba(9, 14, 26, 0) 70%);
}

.bg-grid {
  position: absolute;
  width: 200%;
  height: 200%;
  background-image: linear-gradient(rgba(255, 255, 255, 0.02) 1px,
      transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 30px 30px;
  transform: perspective(500px) rotateX(60deg);
  animation: grid-move 15s linear infinite;
  top: 0;
  left: -50%;
}

@keyframes grid-move {
  0% {
    transform: perspective(500px) rotateX(60deg) translateY(0);
  }

  100% {
    transform: perspective(500px) rotateX(60deg) translateY(30px);
  }
}

.floating-orbs {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  overflow: hidden;
}

.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(50px);
  opacity: 0.3;
  animation: float 20s ease-in-out infinite alternate;
}

.orb:nth-child(1) {
  width: 500px;
  height: 500px;
  background: var(--primary);
  top: -200px;
  right: -100px;
  animation-delay: 0s;
}

.orb:nth-child(2) {
  width: 400px;
  height: 400px;
  background: var(--secondary);
  bottom: -150px;
  left: -150px;
  animation-delay: -5s;
}

.orb:nth-child(3) {
  width: 300px;
  height: 300px;
  background: var(--accent);
  bottom: 20%;
  right: 10%;
  animation-delay: -10s;
}

@keyframes float {
  0% {
    transform: translate(0, 0);
  }

  100% {
    transform: translate(30px, 30px);
  }
}

/* Container */
.container {
  width: 100%;
  height: auto;
  max-width: 85%;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 10;
}

/* Navbar */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 0;
  height: 80px;
  backdrop-filter: blur(30px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  margin-bottom: 2rem;
  /* background: rgba(255, 255, 255, 0.02); */
  animation: navFade 1s cubic-bezier(0.65, 0, 0.35, 1) forwards;
  position: relative;
  z-index: 10;
}

.logo {
  display: flex;
  align-items: center;
  /* gap: 12px; */
  font-size: 1.8rem;
  font-weight: 700;
  font-family: "Amazon Ember", "Helvetica Neue", Arial, "Roboto", "Open Sans", sans-serif;
  letter-spacing: 0em;
  color: var(--light);
  text-decoration: none;
  transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1), color 0.4s ease;
  animation: logoPop 1.2s ease forwards;
  will-change: transform, color;
}

.logo:hover {
  transform: scale(1.12) rotate(3deg);
  color: var(--accent);
}

/* Logo Icon */
.logo-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 46px;
  height: 46px;
  background: var(--gradient);
  border-radius: 14px;
  box-shadow: 0 12px 30px rgba(58, 134, 255, 0.4);
  position: relative;
  overflow: hidden;
  animation: float 3s ease-in-out infinite;
}

.logo-icon::after {
  content: '';
  position: absolute;
  width: 160%;
  height: 160%;
  background: linear-gradient(120deg,
      transparent,
      rgba(255, 255, 255, 0.25),
      transparent);
  transform: translateX(-100%);
  animation: shine 2.8s infinite linear;
}

/* Navigation Links */
.nav-links {
  display: flex;
  align-items: center;
  gap: 3.5rem;
  margin-right: auto;
  margin-left: 6rem;
  animation: navFade 1.4s ease forwards;
}

.nav-link {
  font-size: 1rem;
  color: rgba(248, 249, 250, 0.8);
  text-decoration: none;
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  font-weight: 500;
  letter-spacing: 0.4px;
  padding: 10px 0;
  opacity: 0.85;
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 0%;
  height: 2px;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  background: var(--gradient);
  transition: width 0.5s ease;
  border-radius: 2px;
}

.nav-link:hover {
  color: var(--light);
  transform: translateY(-4px) scale(1.08);
  opacity: 1;
}

.nav-link:hover::after {
  width: 100%;
}

.nav-link.active {
  color: var(--light);
  font-weight: 700;
  transform: scale(1.05);
}

.nav-link.active::after {
  width: 100%;
  height: 3px;
  background: var(--accent);
  box-shadow: 0 0 10px rgba(255, 0, 110, 0.6);
}

/* Auth Buttons */
.auth-buttons {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  animation: navFade 1.6s ease forwards;
}

.login-btn {
  padding: 0.8rem 1.6rem;
  font-size: 1rem;
  font-weight: 600;
  color: var(--light);
  background: var(--glass);
  border: 2px solid rgba(255, 255, 255, 0.15);
  border-radius: 80px;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  backdrop-filter: blur(12px);
  transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
  position: relative;
  overflow: hidden;
  will-change: transform, box-shadow;
}

.login-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -120%;
  width: 120%;
  height: 100%;
  background: linear-gradient(120deg,
      transparent,
      rgba(255, 255, 255, 0.25),
      transparent);
  transition: left 0.6s ease;
}

.login-btn:hover::before {
  left: 120%;
}

.login-btn:hover {
  transform: translateY(-6px) scale(1.07);
  box-shadow: 0 18px 35px rgba(0, 0, 0, 0.35);
}

/* Small ripple click effect */
.login-btn::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 20px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  pointer-events: none;
}

.login-btn:hover::after {
  animation: ripple 0.7s linear forwards;
}

/* Animations */
@keyframes shine {
  0% {
    transform: translateX(-100%);
  }

  100% {
    transform: translateX(100%);
  }
}

@keyframes navFade {
  0% {
    opacity: 0;
    transform: translateY(-30px) scale(0.95);
  }

  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@keyframes logoPop {
  0% {
    opacity: 0;
    transform: scale(0.8) rotate(-10deg);
  }

  100% {
    opacity: 1;
    transform: scale(1) rotate(0deg);
  }
}

@keyframes float {

  0%,
  100% {
    transform: translateY(0px);
  }

  50% {
    transform: translateY(-5px);
  }
}

@keyframes ripple {
  0% {
    transform: translate(-50%, -50%) scale(0.8);
    opacity: 0.5;
  }

  100% {
    transform: translate(-50%, -50%) scale(3);
    opacity: 0;
  }
}

/* Hero Section */
.hero {
  display: grid;
  grid-template-columns: 1fr 1fr;
  height: calc(100vh - 80px);
  align-items: center;
}

.hero-content {
  max-width: 600px;
}

.hero-subtitle {
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--primary-light);
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 8px;
  opacity: 0;
  transform: translateY(20px);
  animation: fade-up 0.5s ease forwards;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 1.5rem;
  opacity: 0;
  transform: translateY(20px);
  animation: fade-up 0.5s ease forwards 0.2s;
}

.hero-description {
  font-size: 1.1rem;
  line-height: 1.6;
  color: rgba(248, 249, 250, 0.8);
  margin-bottom: 2rem;
  opacity: 0;
  transform: translateY(20px);
  animation: fade-up 0.5s ease forwards 0.4s;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  opacity: 0;
  transform: translateY(20px);
  animation: fade-up 0.5s ease forwards 0.6s;
}

.features-pill {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 3rem;
  opacity: 0;
  transform: translateY(20px);
  animation: fade-up 0.5s ease forwards 0.8s;
}

.feature {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 0.5rem 1rem;
  background: var(--glass);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 100px;
  font-size: 0.9rem;
  backdrop-filter: blur(10px);
}

.feature-icon {
  width: 16px;
  height: 16px;
  fill: var(--primary-light);
}

/* Dashboard Mockup */
.hero-visual {
  position: relative;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.dashboard-wrapper {
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  perspective: 1000px;
  transform-style: preserve-3d;
  opacity: 0;
  animation: fade-in 1s ease forwards 0.8s;
}

.dashboard {
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: var(--shadow);
  transform: rotateY(-15deg) rotateX(5deg);
  transform-style: preserve-3d;
  transition: transform 0.5s ease;
  animation: float-dashboard 5s ease-in-out infinite alternate;
}

.dashboard-wrapper:hover .dashboard {
  transform: rotateY(-5deg) rotateX(2deg);
}

@keyframes float-dashboard {
  0% {
    transform: rotateY(-15deg) rotateX(5deg) translateY(0);
  }

  100% {
    transform: rotateY(-15deg) rotateX(5deg) translateY(-20px);
  }
}

.dashboard-content {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.dashboard-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: white;
}

.dashboard-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  flex: 1;
}

.stat-card {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.stat-title {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.6);
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: white;
}

.expenses-chart {
  grid-column: span 2;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1rem;
  height: 180px;
  position: relative;
  overflow: hidden;
}

.chart-title {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 1rem;
}

.chart {
  height: calc(100% - 2rem);
  width: 100%;
  display: flex;
  align-items: flex-end;
  gap: 12px;
  padding-top: 1rem;
}

.chart-bar {
  flex: 1;
  background: var(--gradient);
  border-radius: 4px 4px 0 0;
  position: relative;
  animation: grow-height 1.5s ease-out forwards;
  transform-origin: bottom;
  opacity: 0.8;
}

.chart-bar:hover {
  opacity: 1;
}

.chart-bar:nth-child(1) {
  height: 40%;
  animation-delay: 0s;
}

.chart-bar:nth-child(2) {
  height: 65%;
  animation-delay: 0.1s;
}

.chart-bar:nth-child(3) {
  height: 45%;
  animation-delay: 0.2s;
}

.chart-bar:nth-child(4) {
  height: 80%;
  animation-delay: 0.3s;
}

.chart-bar:nth-child(5) {
  height: 60%;
  animation-delay: 0.4s;
}

.chart-bar:nth-child(6) {
  height: 75%;
  animation-delay: 0.5s;
}

.chart-bar:nth-child(7) {
  height: 50%;
  animation-delay: 0.6s;
}

@keyframes grow-height {
  from {
    transform: scaleY(0);
  }

  to {
    transform: scaleY(1);
  }
}

.transactions {
  grid-column: span 2;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  flex: 1;
  overflow: hidden;
}

.transaction-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
  transition: transform 0.3s ease;
  animation: slide-in 0.5s ease forwards;
  opacity: 0;
  transform: translateX(-20px);
}

.transaction-item:hover {
  transform: translateX(5px);
  background: rgba(255, 255, 255, 0.05);
}

.transaction-item:nth-child(1) {
  animation-delay: 1s;
}

.transaction-item:nth-child(2) {
  animation-delay: 1.1s;
}

.transaction-item:nth-child(3) {
  animation-delay: 1.2s;
}

.transaction-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.transaction-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.1);
}

.transaction-details {
  display: flex;
  flex-direction: column;
}

.transaction-name {
  font-size: 0.9rem;
  font-weight: 500;
}

.transaction-date {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.5);
}

.transaction-amount {
  font-weight: 600;
  color: #ff006e;
}

/* Animations */
@keyframes fade-up {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-in {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes slide-in {
  from {
    opacity: 0;
    transform: translateX(-20px);
  }

  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Floating Data Points */
.data-points {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.data-point {
  position: absolute;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--primary);
  box-shadow: 0 0 10px var(--primary);
  opacity: 0;
  animation: pulse 3s ease-in-out infinite, float-point 15s ease-in-out infinite;
}

.data-point:nth-child(1) {
  top: 20%;
  left: 10%;
  animation-delay: 0s, 0s;
}

.data-point:nth-child(2) {
  top: 70%;
  left: 20%;
  animation-delay: 0.5s, 2s;
}

.data-point:nth-child(3) {
  top: 40%;
  left: 80%;
  animation-delay: 1s, 4s;
}

.data-point:nth-child(4) {
  top: 60%;
  left: 60%;
  animation-delay: 1.5s, 6s;
}

.data-point:nth-child(5) {
  top: 30%;
  left: 90%;
  animation-delay: 2s, 8s;
}

@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 0.8;
  }

  50% {
    transform: scale(1.5);
    opacity: 0.4;
  }

  100% {
    transform: scale(1);
    opacity: 0.8;
  }
}

@keyframes float-point {
  0% {
    transform: translate(0, 0);
  }

  33% {
    transform: translate(10px, 10px);
  }

  66% {
    transform: translate(-10px, 5px);
  }

  100% {
    transform: translate(0, 0);
  }
}

/* Services Section Styles */
.services-section {
  padding: 100px 0;
  background-color: var(--dark);
  position: relative;
  overflow: hidden;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.services-section.section-visible {
  opacity: 1;
  transform: translateY(0);
}

.section-header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 60px;
}

.section-label {
  display: inline-block;
  padding: 8px 16px;
  background: rgba(58, 134, 255, 0.1);
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--primary);
  margin-bottom: 16px;
  position: relative;
  overflow: hidden;
}

.section-label::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg,
      transparent,
      rgba(255, 255, 255, 0.2),
      transparent);
  animation: shine 3s infinite;
}

@keyframes shine {
  0% {
    left: -100%;
  }

  50% {
    left: 100%;
  }

  100% {
    left: 100%;
  }
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 20px;
  background: linear-gradient(135deg,
      var(--light) 0%,
      rgba(255, 255, 255, 0.7) 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.section-description {
  font-size: 1.1rem;
  color: rgba(248, 249, 250, 0.7);
  line-height: 1.6;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  margin-bottom: 80px;
}

.service-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  padding: 30px;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative;
  z-index: 1;
  overflow: hidden;
  opacity: 0;
  transform: translateY(30px);
}

.service-card.fade-in-up {
  animation: fadeInUp 0.8s forwards;
}

.service-card:nth-child(1) {
  animation-delay: 0.1s;
}

.service-card:nth-child(2) {
  animation-delay: 0.3s;
}

.service-card:nth-child(3) {
  animation-delay: 0.5s;
}

.service-card:nth-child(4) {
  animation-delay: 0.7s;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.service-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 50% 0%,
      rgba(58, 134, 255, 0.1),
      transparent 70%);
  opacity: 0;
  transition: opacity 0.4s ease;
  z-index: -1;
}

.service-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
  border-color: rgba(58, 134, 255, 0.3);
}

.service-card:hover::before {
  opacity: 1;
}

.service-icon-wrapper {
  margin-bottom: 24px;
  position: relative;
  width: 60px;
  height: 60px;
}

.service-icon {
  width: 60px;
  height: 60px;
  border-radius: 16px;
  background: var(--gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 10px 20px rgba(26, 68, 133, 0.3);
  position: relative;
  overflow: hidden;
}

.service-icon::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle,
      rgba(255, 255, 255, 0.3) 0%,
      transparent 70%);
  opacity: 0;
  transition: opacity 0.4s;
  pointer-events: none;
}

.service-card:hover .service-icon::after {
  opacity: 1;
}

.service-title {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 16px;
  color: var(--light);
}

.service-description {
  font-size: 1rem;
  color: rgba(248, 249, 250, 0.7);
  line-height: 1.6;
  margin-bottom: 20px;
}

.service-link {
  display: flex;
  align-items: center;
  color: var(--primary);
  font-weight: 500;
  font-size: 0.95rem;
  text-decoration: none;
  transition: all 0.3s ease;
}

.service-link svg {
  margin-left: 8px;
  transition: transform 0.3s ease;
}

.service-link:hover {
  color: #5598ff;
}

.service-link:hover svg {
  transform: translateX(5px);
}

.service-highlight {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 24px;
  padding: 50px;
  position: relative;
  overflow: hidden;
}

.service-highlight::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 30% 30%,
      rgba(58, 134, 255, 0.15),
      transparent 70%);
  z-index: -1;
}

.highlight-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.highlight-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 20px;
  color: var(--light);
}

.highlight-description {
  font-size: 1.1rem;
  color: rgba(248, 249, 250, 0.8);
  line-height: 1.6;
  margin-bottom: 30px;
}

.btn {
  display: inline-flex;
  align-items: center;
  padding: 14px 28px;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
}

.btn svg {
  margin-left: 8px;
  transition: transform 0.3s ease;
}

.btn-primary {
  background: var(--gradient);
  color: white;
  border: none;
  box-shadow: 0 10px 25px -5px rgba(58, 134, 255, 0.5);
}

.btn-primary:hover {
  box-shadow: 0 15px 30px -5px rgba(58, 134, 255, 0.7);
  transform: translateY(-2px);
}

.btn-primary:hover svg {
  transform: translateX(5px);
}

.highlight-visual {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.phone-mockup {
  width: 300px;
  height: 600px;
  background: linear-gradient(145deg, #2b2c3e, #1e1f2e);
  border-radius: 40px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4), 0 0 40px rgba(58, 134, 255, 0.2);
  padding: 12px;
  transition: transform 0.5s ease;
}

.phone-screen {
  background-color: #0d0e15;
  height: 100%;
  border-radius: 32px;
  overflow: hidden;
  position: relative;
}

.phone-notch {
  position: absolute;
  top: 3%;
  left: 50%;
  transform: translate(-50%);
  /* width: 150px; */
  height: 25px;
  background-color: #1e1f2e;
  border-bottom-left-radius: 32px;
  border-top-right-radius: 32px;
  border-top-left-radius: 32px;
  border-bottom-right-radius: 32px;
  width: 30%;
  z-index: 1;

}

.phone-button {
  position: absolute;
  top: 40%;
  right: -2px;
  width: 4px;
  height: 60px;
  background-color: #333;
  border-top-left-radius: 2px;
  border-bottom-left-radius: 2px;
}

.glow-effect {
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  border-radius: 40px;
  box-shadow: inset 0 0 20px rgba(58, 134, 255, 0.3);
  pointer-events: none;
}

/* Audio message styling */
.audio-message {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  background: var(--primary);
  border-radius: 16px;
  color: white;
}

.audio-waveform {
  display: flex;
  align-items: center;
  gap: 2px;
  height: 20px;
}

.audio-waveform span {
  display: inline-block;
  width: 3px;
  height: 10px;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 1px;
}

.audio-waveform span:nth-child(1) {
  height: 5px;
}

.audio-waveform span:nth-child(2) {
  height: 12px;
}

.audio-waveform span:nth-child(3) {
  height: 18px;
}

.audio-waveform span:nth-child(4) {
  height: 10px;
}

.audio-waveform span:nth-child(5) {
  height: 7px;
}

.audio-duration {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.8);
}

/* Voice button styling */
.voice-button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--secondary);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  border: none;
  margin-left: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.voice-button:hover {
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(131, 56, 236, 0.5);
}

.expense-item {
  font-weight: 500;
  color: rgba(255, 255, 255, 0.95);
}

.chat-message .message-text {
  line-height: 1.4;
}

.chat-message.bot strong {
  color: var(--primary-light);
}

.chat-message.bot em {
  color: var(--accent);
  font-style: italic;
}

.chat-interface {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.chat-header {
  display: flex;
  align-items: center;
  padding: 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.chat-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--gradient);
  margin-right: 12px;
}

.chat-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
}

.chat-messages {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
  scrollbar-width: none;
}

.chat-message {
  max-width: 80%;
  padding: 12px 16px;
  border-radius: 16px;
  font-size: 0.95rem;
  line-height: 1.5;
}

.chat-message.user {
  align-self: flex-end;
  background: var(--primary);
  color: white;
  border-bottom-right-radius: 4px;
}

.chat-message.bot {
  align-self: flex-start;
  background: rgba(255, 255, 255, 0.05);
  color: rgba(255, 255, 255, 0.9);
  border-bottom-left-radius: 4px;
}

.typing-indicator {
  display: flex;
  align-items: center;
  gap: 4px;
  height: 20px;
}

.typing-indicator span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.6);
  animation: typing 1.5s infinite;
}

.typing-indicator span:nth-child(1) {
  animation-delay: 0s;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.5s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 1s;
}

@keyframes typing {

  0%,
  100% {
    transform: translateY(0);
    opacity: 0.6;
  }

  50% {
    transform: translateY(-5px);
    opacity: 1;
  }
}

.chat-input {
  display: flex;
  align-items: center;
  padding: 15px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.chat-input input {
  flex: 1;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 24px;
  padding: 12px 16px;
  color: white;
  font-size: 0.85rem;
  width: 40%;
  outline: none;
  transition: all 0.3s ease;
}

.chat-input input:focus {
  border-color: rgba(58, 134, 255, 0.5);
  box-shadow: 0 0 0 2px rgba(58, 134, 255, 0.2);
}

.send-button {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: var(--gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  border: none;
  margin-left: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.send-button:hover {
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(58, 134, 255, 0.5);
}

/* Testimonials Section Styles */
.testimonials-section {
  padding: 100px 0;
  background-color: var(--dark);
  position: relative;
  overflow: hidden;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.testimonials-section.section-visible {
  opacity: 1;
  transform: translateY(0);
}

.testimonials-slider {
  position: relative;
  max-width: 1000px;
  margin: 0 auto;
  overflow: hidden;
}

.testimonial-track {
  display: flex;
  gap: 24px;
  transition: transform 0.5s ease;
}

.testimonial-card {
  min-width: calc(100% - 48px);
  height: 280px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 20px;
  overflow: hidden;
  flex-shrink: 0;
  transition: all 0.4s ease;
}

.testimonial-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  border-color: rgba(58, 134, 255, 0.2);
}

.testimonial-content {
  padding: 30px;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.quote-icon {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  background: rgba(58, 134, 255, 0.1);
  color: var(--primary);
  margin-bottom: 20px;
}

.testimonial-text {
  flex: 1;
  font-size: 1.1rem;
  color: rgba(248, 249, 250, 0.9);
  line-height: 1.7;
  margin-bottom: 24px;
  font-style: italic;
}

.testimonial-author {
  display: flex;
  align-items: center;
}

.author-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(45deg, #5598ff, #7747ff);
  margin-right: 16px;
}

.author-name {
  font-weight: 600;
  color: var(--light);
  margin-bottom: 4px;
}

.author-title {
  font-size: 0.9rem;
  color: rgba(248, 249, 250, 0.6);
}

.slider-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 40px;
  gap: 20px;
}

.slider-arrow {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: var(--light);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
}

.slider-arrow:hover {
  background: rgba(58, 134, 255, 0.1);
  border-color: rgba(58, 134, 255, 0.3);
  color: var(--primary);
}

.slider-dots {
  display: flex;
  gap: 8px;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  cursor: pointer;
  transition: all 0.3s ease;
}

.dot.active {
  background: var(--primary);
  transform: scale(1.2);
  box-shadow: 0 0 10px rgba(58, 134, 255, 0.5);
}

/* Footer Styles */
.footer {
  background-color: #080a1a;
  position: relative;
  padding: 80px 0 40px;
  overflow: hidden;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

.footer.section-visible {
  opacity: 1;
  transform: translateY(0);
}

.footer-gradient {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 200px;
  background: linear-gradient(180deg, var(--dark) 0%, #080a1a 100%);
}

.footer-top {
  display: grid;
  grid-template-columns: 1.5fr 3fr;
  gap: 60px;
  position: relative;
  z-index: 1;
  margin-bottom: 60px;
}

.footer-brand {
  max-width: 280px;
}

.footer-logo {
  display: flex;
  align-items: center;
  font-size: 1.6rem;
  font-weight: 700;
  color: white;
  text-decoration: none;
  margin-bottom: 20px;
}

.logo-icon {
  margin-right: 10px;
  background: var(--gradient);
  width: 36px;
  height: 36px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.footer-tagline {
  font-size: 1rem;
  color: rgba(248, 249, 250, 0.7);
  line-height: 1.6;
  margin-bottom: 25px;
}

.social-links {
  display: flex;
  gap: 12px;
}

.social-link {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.05);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(248, 249, 250, 0.8);
  transition: all 0.3s ease;
}

.social-link:hover {
  background: var(--gradient);
  color: white;
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}


.footer-subscribe {
  margin-bottom: 60px;
  position: relative;
  z-index: 1;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  padding: 30px;
}

.subscribe-title {
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--light);
  margin-bottom: 12px;
}

.subscribe-text {
  font-size: 1rem;
  color: rgba(248, 249, 250, 0.7);
  margin-bottom: 24px;
}

.subscribe-form {
  display: flex;
  gap: 12px;
}

.subscribe-form input {
  flex: 1;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 14px 20px;
  color: white;
  font-size: 1rem;
  outline: none;
  transition: all 0.3s ease;
}

.subscribe-form input:focus {
  border-color: rgba(58, 134, 255, 0.5);
  box-shadow: 0 0 0 2px rgba(58, 134, 255, 0.2);
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 40px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  position: relative;
  z-index: 1;
}

.copyright {
  color: rgba(248, 249, 250, 0.5);
  font-size: 0.9rem;
}

.footer-badges {
  display: flex;
  gap: 20px;
}

.badge {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.9rem;
  color: rgba(248, 249, 250, 0.7);
}
</style>