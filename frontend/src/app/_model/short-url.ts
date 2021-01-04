export class ShortUrl {
  constructor(
    // tslint:disable-next-line:variable-name
    public originalUrl: string,
    public slug?: string,
    public password?: any,
    public visits?: number,
    public createdAt?: Date

  ) {
  }
}
