import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'mediaFilter'
})
export class MediaFilterPipe implements PipeTransform {

  transform(items: any[], search: string): any {
    if (!search) {
      return items;
    }

    search = search.trim();

    const results = [];
    for (const item of items) {
      if (item.title && item.title.match(RegExp(search, 'i'))) {
        results.push(item);
      } else if (item.Title && item.Title.match(RegExp(search, 'i'))) {
        results.push(item);
      } else if (item.name && item.name.match(RegExp(search, 'i'))) {
        results.push(item);
      } else if (item.release_date && item.release_date.match(RegExp(search, 'i'))) {
        results.push(item);
      }
    }
    return results;
  }
}
