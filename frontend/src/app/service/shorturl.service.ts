import { Injectable } from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {ShortUrl} from '../_model/short-url';
import {environment} from '../../environments/environment';
import {catchError} from 'rxjs/operators';
import {Router} from '@angular/router';
import {User} from '../_model/user';

@Injectable({
  providedIn: 'root'
})
export class ShorturlService {
  API_URL = environment.API_URL;


  constructor(private httpClient: HttpClient, private router: Router) { }



  // tslint:disable-next-line:typedef
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  getShortUrl(slug: string): Observable<ShortUrl> {
  return this.httpClient
      .get<ShortUrl>(`${this.API_URL}/api/link${slug}`);

}
createShortUrl( data: ShortUrl): Observable<ShortUrl>{
    return this.httpClient
      .post<ShortUrl>(`${this.API_URL}/api/link`, data);
}
getUser(): Observable<User> {
    return this.httpClient
      .get<User>(`${this.API_URL}/api/user`);
}

updateApiKey(): Observable<User>{
    return this.httpClient
      .put<User>(`${this.API_URL}/api/user`, {});
}
}
