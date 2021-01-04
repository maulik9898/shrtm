import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import { AppComponent } from './app.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {ShorturlService} from './service/shorturl.service';
import { NotFoundComponent } from './not-found/not-found.component';
import { CreateShortUrlComponent } from './create-short-url/create-short-url.component';
import { GetShortUrlComponent } from './get-short-url/get-short-url.component';
import { LoginComponent } from './login/login.component';

import { AngularFireModule } from '@angular/fire';
import { AngularFireAuthModule } from '@angular/fire/auth';
import { environment } from '../environments/environment';
import {AuthService} from './service/auth.service';
import { SignUpComponent } from './sign-up/sign-up.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import {AuthGuard} from './auth.guard';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { SettingsComponent } from './settings/settings.component';
import {TokenInterceptor} from './_interceptor/token.interceptor';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { HeaderComponent } from './header/header.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';



const routes: Routes = [
   {path: 'not-found', component: NotFoundComponent},
  {path: 'sign-in', component: LoginComponent},
  {path: 'sign-up', component: SignUpComponent},
  {path: '', component: DashboardComponent},
  {path: 'settings', component: SettingsComponent, canActivate: [AuthGuard]}

];

@NgModule({
  declarations: [
    AppComponent,
    NotFoundComponent,
    CreateShortUrlComponent,
    GetShortUrlComponent,
    LoginComponent,
    SignUpComponent,
    DashboardComponent,
    SettingsComponent,
    HeaderComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    RouterModule.forRoot(routes),
    AngularFireModule.initializeApp(environment.firebase),
    AngularFireAuthModule,
    FormsModule,
    ReactiveFormsModule,
    NgbModule,
    FontAwesomeModule
  ],
  providers: [
    ShorturlService,
    AuthService,
    { provide: HTTP_INTERCEPTORS, useClass: TokenInterceptor, multi: true }],
  bootstrap: [AppComponent]
})
export class AppModule {

}
